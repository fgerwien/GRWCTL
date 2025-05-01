import os

class GRWConfig:
    # General settings
    APP_NAME = "GRWCTL"
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

    # Database settings
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME", "grwctl_db")
    DB_USER = os.getenv("DB_USER", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG" if DEBUG else "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "/var/log/grwctl.log")

    # Other settings
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", 30))
    SENSOR_INTERVAL = int(os.getenv("SENSOR_INTERVAL", 60))


class PINConfig:
    # GPIO pin configuration
    DHT22_SENSOR1_NAME = os.getenv("DHT22_SENSOR1_NAME", "DHT22 Sensor 1")
    DHT22_SENSOR1_PIN = int(os.getenv("DHT22_SENSOR1_PIN", 26))

    DHT22_SENSOR2_NAME = os.getenv("DHT22_SENSOR2_NAME", "DHT22 Sensor 2")
    DHT22_SENSOR2_PIN = int(os.getenv("DHT22_SENSOR2_PIN", 21))
    
    BME280_SENSOR_NAME = os.getenv("BME280_SENSOR_NAME", "BME280 Sensor")
    BME280_I2C_ADDRESS = int(os.getenv("BME280_I2C_ADDRESS", 0x76))
    BME280_I2C_BUS = int(os.getenv("BME280_I2C_BUS", 1))
    
    MOISTURE_SENSOR_NAME = os.getenv("MOISTURE_SENSOR_NAME", "Moisture Sensor")
    MOISTURE_SENSOR_PIN = int(os.getenv("MOISTURE_SENSOR_PIN", 6))


if __name__ == "__main__":
    # This will print the configuration values when this script is run directly.
    for key, value in GRWConfig.__dict__.items():
        if not key.startswith("__"):
            print(f"{key}: {value}")
    print("\nPIN Configuration:")
    for key, value in PINConfig.__dict__.items():
        if not key.startswith("__"):
            print(f"{key}: {value}")
