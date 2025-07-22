import os

from utils import load_envconfig

load_envconfig()


class GRWConfig:
    # General settings
    APP_NAME = "GRWCTL"
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

    # Database settings
    INFLUXDB_HOST = os.getenv("INFLUXDB_HOST", "localhost")
    INFLUXDB_PORT = int(os.getenv("INFLUXDB_PORT", 8086))
    INFLUXDB_DATABASE = os.getenv("INFLUXDB_DATABASE", "grwctl_db")
    INFLUXDB_USER = os.getenv("INFLUXDB_USER", "user")
    INFLUXDB_PASSWORD = os.getenv("INFLUXDB_PASSWORD", "password")
    INFLUXDB_RETENTION_POLICY = os.getenv("INFLUXDB_RETENTION_POLICY", "26w")

    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG" if DEBUG else "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "grwctl.log")

    # Other settings
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", 30))
    SENSOR_INTERVAL = int(os.getenv("SENSOR_INTERVAL", 60))


class PINConfig:
    # GPIO pin configuration
    DHT22_SENSOR1_NAME = os.getenv("DHT22_SENSOR1_NAME", "DHT22 Sensor 1")
    DHT22_SENSOR1_PIN = int(os.getenv("DHT22_SENSOR1_PIN", 26))

    DHT22_SENSOR2_NAME = os.getenv("DHT22_SENSOR2_NAME", "DHT22 Sensor 2")
    DHT22_SENSOR2_PIN = int(os.getenv("DHT22_SENSOR2_PIN", 21))

    BME280_SENSOR_NAME = os.getenv("BME280_SENSOR_NAME", "BME280 Sensor")
    BME280_I2C_ADDRESS = int(os.getenv("BME280_I2C_ADDRESS", 0x76), 16)

    MOISTURE_SENSOR_NAME = os.getenv("MOISTURE_SENSOR_NAME", "Moisture Sensor")
    MOISTURE_SENSOR_PIN = int(os.getenv("MOISTURE_SENSOR_PIN", 6))
