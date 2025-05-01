import time

import adafruit_dht
import board


class DHT22Sensor:
    def __init__(self, pin, name):
        # Map the pin number to the appropriate board pin
        self.pin = getattr(board, f"D{pin}")
        self.sensor = adafruit_dht.DHT22(self.pin)
        self.name = name
        self.retries = 5
        self.retry_delay = 2

    def read_data(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity
            if humidity is not None and temperature is not None:
                return {"temperature": temperature, "humidity": humidity}
            else:
                return {"error": f"Failed to read from DHT22 on pin {self.pin}"}
        except RuntimeError as e:
            # Handle the 'Try-Again' errors ...
            if "Try again" in str(e):
                # Retry reading the sensor
                for _ in range(self.retries):
                    try:
                        temperature = self.sensor.temperature
                        humidity = self.sensor.humidity
                        if humidity is not None and temperature is not None:
                            return {"temperature": temperature, "humidity": humidity}
                    except RuntimeError:
                        pass
                    time.sleep(self.retry_delay)
            return {"error": str(e)}
        except Exception as e:
            # Handle other exceptions
            return {"error": f"Unexpected error: {str(e)}"}
