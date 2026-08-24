from pathlib import Path

from setuptools import find_packages, setup

# Read requirements from requirements.txt
requirements_path = Path(__file__).parent / "requirements.txt"
with requirements_path.open() as f:
    requirements = f.read().splitlines()

setup(
    name="GRWCTL",
    version="0.1.0",
    author="Florian Gerwien",
    author_email="grwctl@web-playground.com",
    description="A project to read sensor data from Raspberry Pi and log it to InfluxDB",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "sensor-reader=main:main",  # Assuming main function is defined in main.py
        ],
    },
)
