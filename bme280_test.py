import time
import smbus2
import bme280
import board
import adafruit_ltr390

class BME280Sensor:
    def __init__(self, address=0x76):
        self.address=address
        self.bus=smbus2.SMBus(1)
        self.calibration_param=mbe280.load_calibration_params(self.bus, self.address)

    def read_data(self):
        data = bme280.sample(self.bus, self.address, self.calibration_param)
        return {
            "temperature": data.temperature,
            "pressure": data.pressure,
            "humidity": data.humidity
            }

    def display_data(self):
        data = self.read_data()
        print(f"Temperature = {data['temperature']} °C")
        print(f"Pressure = {data['pressure']} hPa")
        print(f"Humidity = {data['humidity']} %")
        print("*************************")

class LTR390Sensor:
    def __init__(self):
    self.i2c = board.I2C()
    self.ltr = adafruit_ltr390.LTR390(self.i2c)

#address = 0x76

#bus = smbus2.SMBus(1)

#i2c = board.I2C()

#ltr = adafruit_ltr390.LTR390(i2c)

#calibration_param = bme280.load_calibration_params(bus, address)

#while True:
 #   try:
  #      data = bme280.sample(bus, address, calibration_param)

    #    temperature = data.temperature
   #     pressure = data.pressure
     #   humidity = data.humidity

      #  uv_intensity = ltr.uvs  # UV sensor value (raw or calibrated depending on the sensor settings)
       # ambient_light = ltr.light  # Ambient light intensity in lux

        # Print sensor data
        #print(f'Temperature = {temperature} °C')
        #p#rint(f'Pressure = {pressure} hPa')
#        print(f'Humidity = {humidity} %')
 #       print(f"UV Intensity = {uv_intensity} (RAW or Calibrated)")
  #      print(f"Ambient Light = {ambient_light} lux")
   #     print("*************************")

    #    time.sleep(2)  # Delay for next reading

 #   except Exception as e:
 #       print(f"Error reading sensor data: {e}")
  #      time.sleep(2)

