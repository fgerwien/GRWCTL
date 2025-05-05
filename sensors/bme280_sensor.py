import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

from logger import GRWLogger
from sensors.base import SensorBase


class BME280Sensor(SensorBase):
    def __init__(self, address=0x76, name="BME280"):
        super().__init__(address, name)
        # Initialize I2C bus and BME280 sensor
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        self.sensor = adafruit_bme280.Adafruit_BME280_I2C(self.i2c, address=self.pin)
        self.rounding = 2
        self.logger = GRWLogger()

    def read_data(self):
        try:
            # Read temperature, pressure, and humidity
            temperature = round(self.sensor.temperature, self.rounding)  # Celsius
            pressure = round(self.sensor.pressure, 4)  # hPa
            humidity = round(self.sensor.humidity, self.rounding)  # Percentage
            data = {
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity,
            }
            # Check if the sensor values exceed the thresholds
            if self.check_thresholds(data):
                self.logger.log_info(f"Threshold exceeded for {self.name}: {data}")
            else:
                self.logger.log_debug(
                    f"Sensor data within thresholds for {self.name}: {data}"
                )
            return data
        except Exception as e:
            raise RuntimeError(f"Failed to read BME280 sensor data: {e}")
