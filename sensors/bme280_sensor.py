from config import PINConfig

class BME280Sensor:
    def __init__(self, bus_number=PINConfig.BME280_I2C_ADDRESS, address=PINConfig.BME280_I2C_ADDRESS):
        import smbus2
        from bme280 import BME280
        self.bus = smbus2.SMBus(bus_number)
        self.bme280 = BME280(i2c_dev=self.bus, address=address)

    def read_data(self):
        try:
            data = self.bme280.read_compensated_data()
            temperature = data[0] / 100  # Convert to Celsius
            pressure = data[1] / 25600  # Convert to hPa
            humidity = data[2] / 1024  # Convert to percentage
            return {
                'temperature': temperature,
                'pressure': pressure,
                'humidity': humidity
            }
        except Exception as e:
            raise RuntimeError(f"Failed to read BME280 sensor data: {e}")