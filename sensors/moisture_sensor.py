from RPi import GPIO


class MoistureSensor:
    def __init__(self, pin, name):
        # Initialize the moisture sensor here (e.g., GPIO setup)
        self.pin = pin
        self.name = name

    def read_data(self):
        try:
            # Read moisture level from the sensor
            moisture_level = self._read_moisture()
            return moisture_level
        except Exception as e:
            # Handle any exceptions that occur during reading
            raise RuntimeError(f"Failed to read moisture sensor data: {e}")

    def _read_moisture(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        needs_water = GPIO.input(self.pin)

        GPIO.cleanup()  # Clean up GPIO settings after reading

        return {"moisture": not needs_water}
