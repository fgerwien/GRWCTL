import time
from sensors.dht22_sensor import DHT22Sensor
from sensors.bme280_sensor import BME280Sensor
from sensors.moisture_sensor import MoistureSensor
from influxdb_writer import InfluxDBWriter
from logger import GRWLogger
from config import PINConfig, GRWConfig

def main():
    dht22_sensor1 = DHT22Sensor(pin=PINConfig.DHT22_SENSOR1_PIN)  # GPIO pin for first DHT22
    dht22_sensor2 = DHT22Sensor(pin=PINConfig.DHT22_SENSOR2_PIN)  # GPIO pin for second DHT22
    bme280_sensor = BME280Sensor()  # I2C address for BME280
    moisture_sensor = MoistureSensor(pin=PINConfig.MOISTURE_SENSOR_PIN)  # GPIO pin for moisture sensor

    influx_writer = InfluxDBWriter()
    logger = GRWLogger()

    while True:
        try:
            # Read data from DHT22 sensors
            temp1, humidity1 = dht22_sensor1.read_data()
            temp2, humidity2 = dht22_sensor2.read_data()

            # Read data from BME280 sensor
            temp_bme, humidity_bme, pressure_bme = bme280_sensor.read_data()

            # Read data from moisture sensor
            moisture_level = moisture_sensor.read_data()

            # Prepare data for InfluxDB
            data = {
                PINConfig.DHT22_SENSOR1_NAME: {"temperature": temp1, "humidity": humidity1},
                PINConfig.DHT22_SENSOR2_NAME: {"temperature": temp2, "humidity": humidity2},
                PINConfig.BME280_SENSOR_NAME: {"temperature": temp_bme, "humidity": humidity_bme, "pressure": pressure_bme},
                PINConfig.MOISTURE_SENSOR_NAME: {"moisture_level": moisture_level},
            }

            # Write data to InfluxDB
            influx_writer.write_data(data)

            if GRWConfig.DEBUG or GRWConfig.LOG_LEVEL == "DEBUG":
                # Log the data
                logger.log_info(f"Data written to InfluxDB: {data}")
        
        except KeyboardInterrupt:
            logger.log_info("Program terminated by user.")
            break
        except RuntimeError as e:   # Handle sensor read errors
            logger.log_error(f"Sensor read error: {e}")

        except Exception as e:
            logger.log_error(str(e))

        time.sleep(GRWConfig.SENSOR_INTERVAL)

if __name__ == "__main__":
    main()