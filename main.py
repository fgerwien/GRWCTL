import time

from config import GRWConfig, PINConfig
from influxdb_writer import InfluxDBWriter
from logger import GRWLogger
from sensors.bme280_sensor import BME280Sensor
from sensors.dht22_sensor import DHT22Sensor
from sensors.moisture_sensor import MoistureSensor
from utils import load_envconfig

logger = GRWLogger()


def read_sensor(sensor):
    try:
        sensor_data = sensor.read_data()
        if "error" in sensor_data:
            logger.log_error(
                f"Error reading {sensor.__class__.__name__}: {sensor_data['error']}"
            )
        else:
            return sensor_data
    except Exception as e:
        logger.log_error(
            f"Exception while reading {sensor.__class__.__name__}: {str(e)}"
        )


def main():
    dht22_sensor1 = DHT22Sensor(
        pin=PINConfig.DHT22_SENSOR1_PIN
    )  # GPIO pin for first DHT22
    dht22_sensor2 = DHT22Sensor(
        pin=PINConfig.DHT22_SENSOR2_PIN
    )  # GPIO pin for second DHT22
    bme280_sensor = BME280Sensor(
        address=PINConfig.BME280_I2C_ADDRESS
    )  # I2C address for BME280
    moisture_sensor = MoistureSensor(
        pin=PINConfig.MOISTURE_SENSOR_PIN
    )  # GPIO pin for moisture sensor

    # influx_writer = InfluxDBWriter()
    logger.log_info("Starting sensor data collection...")
    while True:
        try:
            data = {}
            data[PINConfig.DHT22_SENSOR1_NAME] = read_sensor(dht22_sensor1)
            data[PINConfig.DHT22_SENSOR2_NAME] = read_sensor(dht22_sensor2)
            data[PINConfig.BME280_SENSOR_NAME] = read_sensor(bme280_sensor)
            data[PINConfig.MOISTURE_SENSOR_NAME] = read_sensor(moisture_sensor)

            # Write data to InfluxDB
            # influx_writer.full_dump(data)

            logger.log_debug(f"Data written to InfluxDB: {data}")

        except KeyboardInterrupt:
            logger.log_info("Program terminated by user.")
            break
        except RuntimeError as e:  # Handle sensor read errors
            logger.log_error(f"Sensor read error: {e}")

        except Exception as e:
            logger.log_error(str(e))

        time.sleep(GRWConfig.SENSOR_INTERVAL)


if __name__ == "__main__":
    load_envconfig()
    main()
