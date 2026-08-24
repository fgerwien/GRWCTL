from gpiozero import DigitalInputDevice

from sensors.base import SensorBase


class MoistureSensor(SensorBase):

    def __init__(self, pin, name):
        super().__init__(pin, name)
        self.sensor = DigitalInputDevice(pin, pull_up=False)

    def read_data(self):
        try:
            # Read moisture level from the sensor
            moisture_level = self._read_moisture()
            return moisture_level
        except Exception as e:
            # Handle any exceptions that occur during reading
            raise RuntimeError(f"Failed to read moisture sensor data: {e}")

    def _read_moisture(self):
        return {"moisture": not self.sensor.is_active}
