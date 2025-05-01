import board
import busio
from adafruit_bme280 import basic as adafruit_bme280


class BME280Sensor:
    def __init__(self, name, address=0x76):
        # Initialize I2C bus and BME280 sensor
        self.name = name
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        self.address = address
        self.sensor = adafruit_bme280.Adafruit_BME280_I2C(
            self.i2c, address=self.address
        )

    def read_data(self):
        try:
            # Read temperature, pressure, and humidity
            temperature = self.sensor.temperature  # Celsius
            pressure = self.sensor.pressure  # hPa
            humidity = self.sensor.humidity  # Percentage
            return {
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity,
            }
        except Exception as e:
            raise RuntimeError(f"Failed to read BME280 sensor data: {e}")
