class InfluxDBWriter:
    def __init__(self, influxdb_client):
        self.influxdb_client = influxdb_client

    def write_data(self, measurement, data):
        try:
            json_body = [
                {
                    "measurement": measurement,
                    "fields": data
                }
            ]
            self.influxdb_client.write_points(json_body)
        except Exception as e:
            from logger import GRWLogger
            logger = GRWLogger()
            logger.log_error(f"Error writing to InfluxDB: {e}")