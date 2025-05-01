# GRWCTL - RaspberryPi-Sensor-Project
This project is designed to read data from multiple sensors connected to a Raspberry Pi, including two DHT22 sensors, BME280 sensor, and a moisture sensor. The collected data is sent to a remote InfluxDB database in a specific interval. Any errors encountered during sensor data reading are logged to a logfile for troubleshooting.

## Project Structure

```
GRWCTL
├── conf
│   └── settings.env
│   └── settings.env.example
├── sensors
│   ├── __init__.py
│   ├── dht22_sensor.py
│   ├── bme280_sensor.py
│   └── moisture_sensor.py
├── main.py
├── config.py
├── influxdb_writer.py
├── logger.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd GRWCTL
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) Install the package:
   ```
   python setup.py install
   ```

## Usage

1. Connect the sensors to the Raspberry Pi according to their specifications.
2. Create a file settings.env or set the configuration (e.g., InfluxDB connection details) as environment variable
3. Run the main script:
   ```
   python main.py
   ```

The script will start reading data from the sensors in a specific interval and log any errors encountered during the process.

## Logging

Errors encountered while reading sensor data will be logged in a logfile.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.