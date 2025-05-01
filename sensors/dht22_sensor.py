import board
import adafruit_dht

class DHT22Sensor:
    def __init__(self, pin):
        # Map the pin number to the appropriate board pin
        self.pin = getattr(board, f"D{pin}")
        self.sensor = adafruit_dht.DHT22(self.pin)

    def read_data(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity
            if humidity is not None and temperature is not None:
                return {'temperature': temperature, 'humidity': humidity}
            else:
                return {'error': f'Failed to read from DHT22 on pin {self.pin}'}
        except RuntimeError as e:
            # Handle occasional read errors
            return {'error': str(e)}
        except Exception as e:
            # Handle other exceptions
            return {'error': f'Unexpected error: {str(e)}'}