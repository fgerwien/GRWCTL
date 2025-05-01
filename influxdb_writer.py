import datetime

from influxdb import InfluxDBClient
from urllib3 import Retry

from config import GRWConfig


class InfluxDBWriter:
    def __init__(self):
        self.influxdb_client = InfluxDBClient(
            host=GRWConfig.INFLUXDB_HOST,
            port=GRWConfig.INFLUXDB_PORT,
            username=GRWConfig.INFLUXDB_USER,
            password=GRWConfig.INFLUXDB_PASSWORD,
            database=GRWConfig.INFLUXDB_DATABASE,
            retries=Retry(connect=5, read=2, redirect=5),
        )
        # self.influxdb_client.create_database(GRWConfig.INFLUXDB_DATABASE)
        # self.influxdb_client.switch_database(GRWConfig.INFLUXDB_DATABASE)
        # self.influxdb_client.create_retention_policy(
        #     GRWConfig.INFLUXDB_RETENTION_POLICY,
        #     GRWConfig.INFLUXDB_RETENTION_DURATION,
        #     replication=1,
        #     default=True
        # )
        # self.influxdb_client.create_continuous_query(
        #     GRWConfig.INFLUXDB_CONTINUOUS_QUERY,
        #     f"SELECT mean(value) INTO {GRWConfig.INFLUXDB_CONTINUOUS_QUERY} FROM {GRWConfig.INFLUXDB_MEASUREMENT} WHERE time > now() - {GRWConfig.INFLUXDB_CONTINUOUS_QUERY_DURATION}",
        #     database=GRWConfig.INFLUXDB_DATABASE
        # )

    def write_data(self, measurement, data):
        try:
            json_body = [{"measurement": measurement, "fields": data}]
            self.influxdb_client.write_points(json_body)
        except Exception as e:
            from logger import GRWLogger

            logger = GRWLogger()
            logger.log_error(f"Error writing to InfluxDB: {e}")

    def full_dump(self, data):
        json_body = []

        for sensor_name, sensor_data in data.items():
            json_body.append(
                {
                    "measurement": GRWConfig.INFLUXDB_DATABASE,
                    "tags": {"sensor": sensor_name},
                    "fields": sensor_data,
                    "time": datetime.datetime.now(datetime.timezone.utc).strftime(
                        "%Y-%m-%dT%H:%M:%SZ"
                    ),
                }
            )

        try:
            self.influxdb_client.write_points(json_body)
        except Exception as e:
            from logger import GRWLogger

            logger = GRWLogger()
            logger.log_error(f"Error writing full_dump to InfluxDB: {e}")
