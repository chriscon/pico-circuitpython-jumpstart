# completely stolen from https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel?gclid=Cj0KCQjwwfiaBhC7ARIsAGvcPe6iyv3z0mItFPkS1IgQNlrJzN37XT9rPbi-o_WKd7M2ot9tpqiKfmcaAimZEALw_wcB
import time
import board
import random
import neopixel

pixel_pin = board.GP28
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)


while True:
    pixels[0] = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
    pixels.show()
    time.sleep(0.1)
