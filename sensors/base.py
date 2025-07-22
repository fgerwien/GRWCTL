class SensorBase:
    """
    Base class for all sensors.
    """

    def __init__(self, pin, name: str):
        self.name = name
        self.pin = pin
        self.old_values = {
            "temperature": None,
            "pressure": None,
            "humidity": None,
            "moisture": None,
        }
        self.threshold = 0.5

    def read_data(self) -> float:
        """
        Read the sensor value.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def check_thresholds(self, value_dict: dict) -> bool:
        """
        Check if the sensor values exceed the thresholds.
        """
        for key, value in value_dict.items():
            if key in self.old_values:
                if self.old_values[key] is None:
                    self.old_values[key] = value
                    continue
                if (self.old_values[key] * self.threshold) < value:
                    self.old_values[key] = value
                    return True
                else:
                    raise ValueError(
                        f"Value {value} is not greater than the threshold {self.old_values[key] * self.threshold} for key: {key}"
                    )
            else:
                raise KeyError(
                    f"Invalid key: {key}. Valid keys are: {list(self.old_values.keys())}"
                )
        return False
