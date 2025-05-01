import datetime

from influxdb import InfluxDBClient
from urllib3 import Retry

from config import GRWConfig
from logger import GRWLogger

logger = GRWLogger()


class InfluxDBWriter:
    def __init__(self):
        # Initialize the InfluxDB client
        self.influxdb_client = InfluxDBClient(
            host=GRWConfig.INFLUXDB_HOST,
            port=GRWConfig.INFLUXDB_PORT,
            database=GRWConfig.INFLUXDB_DATABASE,
            retries=Retry(connect=5, read=2, redirect=5),
        )

        # Check connection
        if not self.influxdb_client.ping():
            logger.log_error("Failed to connect to InfluxDB.")
            raise ConnectionError("Failed to connect to InfluxDB.")
        else:
            logger.log_info("Connected to InfluxDB successfully.")

        # Ensure the database and retention policy exist
        self.ensure_database_and_retention_policy()

    def ensure_database_and_retention_policy(self):
        # Check if the database exists
        databases = self.influxdb_client.get_list_database()
        if GRWConfig.INFLUXDB_DATABASE not in [db["name"] for db in databases]:
            logger.log_info(
                f"Database {GRWConfig.INFLUXDB_DATABASE} does not exist. Creating it."
            )
            self.influxdb_client.create_database(GRWConfig.INFLUXDB_DATABASE)

        # Create the retention policy
        ret_policy = GRWConfig.INFLUXDB_RETENTION_POLICY
        retention_policies = self.influxdb_client.get_list_retention_policies(
            GRWConfig.INFLUXDB_DATABASE
        )
        if ret_policy not in [rp["name"] for rp in retention_policies]:
            logger.log_info(f"Creating retention policy '{ret_policy}'.")
            self.influxdb_client.create_retention_policy(
                name=ret_policy,
                duration=ret_policy,
                replication=1,
                database=GRWConfig.INFLUXDB_DATABASE,
                default=True,
            )

    def write_data(self, measurement, data):
        try:
            json_body = [{"measurement": measurement, "fields": data}]
            self.influxdb_client.write_points(json_body)
        except Exception as e:
            logger.log_error(f"Error writing to InfluxDB: {e}")

    def full_dump(self, data):
        json_body = []
        for sensor_name, sensor_data in data.items():
            json_body.append(
                {
                    "measurement": "sensor_data",
                    "tags": {"sensor": sensor_name},
                    "fields": sensor_data,
                    "time": datetime.datetime.now(datetime.timezone.utc).strftime(
                        "%Y-%m-%dT%H:%M:%SZ"
                    ),
                }
            )

        try:
            logger.log_debug(f"Writing full_dump to InfluxDB: {json_body}")
            self.influxdb_client.write_points(json_body)
        except Exception as e:
            logger.log_error(f"Error writing full_dump to InfluxDB: {e}")
            raise e
        finally:
            logger.log_info("Full dump written to InfluxDB successfully.")
            self.influxdb_client.close()
            logger.log_debug("InfluxDB client closed.")
