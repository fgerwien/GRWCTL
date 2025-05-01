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
        # Placeholder for actual moisture reading logic
        # This should return the moisture level as a float or int
        return {"moisture": True}  # Replace with actual reading logic
