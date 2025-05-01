import os
from dotenv import load_dotenv


def print_config():
    """
    Print the configuration values for debugging purposes.
    """
    from config import GRWConfig, PINConfig
    for key, value in GRWConfig.__dict__.items():
        if not key.startswith("__"):
            print(f"{key}: {value}")
    print("\nPIN Configuration:")
    for key, value in PINConfig.__dict__.items():
        if not key.startswith("__"):
            print(f"{key}: {value}")


def load_envconfig():
    """
    Load configuration from environment variables or default values.
    """
    # Load environment variables from settings.env file
    envfile = os.path.join(os.path.dirname(__file__), "conf/settings.env")
    if os.path.exists(envfile) and load_dotenv(dotenv_path=envfile):
        print(f"Environment variables loaded from {envfile}")
    else:
        print("Environment file not found. Using default settings.")

    if os.getenv("DEBUG"):
        print_config()