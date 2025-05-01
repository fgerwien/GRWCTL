class DHT22Sensor:
    def __init__(self, pin1, pin2):
        import Adafruit_DHT
        self.sensor = Adafruit_DHT.DHT22
        self.pins = [pin1, pin2]

    def read_data(self):
        data = []
        for pin in self.pins:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, pin)
            if humidity is not None and temperature is not None:
                data.append({'temperature': temperature, 'humidity': humidity})
            else:
                data.append({'error': f'Failed to read from DHT22 on pin {pin}'})
        return data