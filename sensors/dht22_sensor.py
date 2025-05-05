import time

import adafruit_dht
import board

from sensors.base import SensorBase


class DHT22Sensor(SensorBase):
    def __init__(self, pin, name):
        # Map the pin number to the appropriate board pin
        super().__init__(pin, name)
        self.pin = getattr(board, f"D{pin}")
        self.sensor = adafruit_dht.DHT22(self.pin)
        self.retries = 5
        self.retry_delay = 2

    def read_data(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity
            if humidity is not None and temperature is not None:
                data = {"temperature": temperature, "humidity": humidity}
                if self.check_thresholds(data):
                    return data
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
                            data = {"temperature": temperature, "humidity": humidity}
                            if self.check_thresholds(data):
                                return data
                    except RuntimeError:
                        pass
                    time.sleep(self.retry_delay)
            return {"error": str(e)}
        except Exception as e:
            # Handle other exceptions
            return {"error": f"Unexpected error: {str(e)}"}
