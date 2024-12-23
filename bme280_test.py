import time
import smbus2
import bme280

class BME280Sensor:
    def __init__(self, bus_number=1, address=0x76):
        self.bus = smbus2.SMBus(bus_number)
        self.address = address
        self.calibration_params = bme280.load_calibration_params(self.bus, self.address)

    def get_data(self):
        """Reads data from the BME280 sensor."""
        data = bme280.sample(self.bus, self.address, self.calibration_params)
        temperature = data.temperature  # in Celsius
        pressure = data.pressure        # in hPa
        humidity = data.humidity        # in %
        return temperature, pressure, humidity

    def read_data(self):
        """Reads and displays the sensor data in a human-readable format."""
        temperature, pressure, humidity = self.get_data()
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Humidity: {humidity:.2f} %")
        print("*************************")

