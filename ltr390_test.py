import time
import board
import adafruit_ltr390

class LTR390Sensor:
    def __init__(self, i2c_bus=None):
        self.i2c = i2c_bus if i2c_bus else board.I2C()
        self.ltr390 = adafruit_ltr390.LTR390(self.i2c)
        

    
    def read_uv_and_light(self):
        uv_light = self.ltr390.uvs  
        ambient_light = self.ltr390.light 
        return  uv_light, ambient_light

    def read_data(self):
        uv_light, ambient_light = self.read_uv_and_light()
        print(f"LTR390 Sensor -> UV Light Intensity: {uv_light}")
        print(f"LTR390 Sensor -> Ambient Light Intensity: {ambient_light}")
        print("*************************")
