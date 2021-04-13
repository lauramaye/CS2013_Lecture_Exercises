# import circuit playground express board
from adafruit_circuitplayground import cp
import time


class NeoPixels: # organised all of our generic neopixel patterns


    def __init__(self):
        self.pixels_off_state = [0, 0, 0]  # pixels are turned off if black.
        self.count = 0
        self.pixel_amount = len(cp.pixels)
        cp.pixels.brightness = 0.1
        cp.pixels.auto_write = False



    def every_second_pixel(self, color):
        for pixel in range(0, self.pixel_amount):
            if pixel % 2 == 0:
                cp.pixels[pixel] = color # pixels positions range from 0 - 9
            else:
                cp.pixels[pixel] = self.pixels_off_state
        cp.pixels.show()

    def wheel(self):
        for pixel in range(self.pixel_amount): # (0, 10)
            cp.pixels[pixel] = [25 * pixel, 0, 100]
            cp.pixels.show()
            time.sleep(0.1) # delay in seconds
            cp.pixels.fill(self.pixels_off_state)
            cp.pixels.show()
        time.sleep(0.5)

class SensorPixels(NeoPixels): # neoPixel patterns only controlled by sensors
    pass


#neopixels_1 = NeoPixels() # __init__(self):
sensor_neopixels_1 = SensorPixels() # __init__(self):
color = [255, 255, 0]
# code to keep running forever
while True:
    sensor_neopixels_1.every_second_pixel(color) # every_second_pixel(self, color):
    time.sleep(0.5)
    sensor_neopixels_1.wheel() # wheel(self):
    time.sleep(0.5)

