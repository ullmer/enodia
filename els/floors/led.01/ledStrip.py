# test code to integrate ledArray library with rpi_ws281x
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-15

import os
from ledArray import *
from rpi_ws281x import *

def ledRun(ledstri,ledarr):
    for i in range(len(ledarr)):
        ledstri.setPixelColor(i,Color(ledarr[i][0],ledarr[i][0],ledarr[i][0]))
    ledstri.show()
    return

#floor configuration
FLOOR_X = 12
FLOOR_Y = 12

# LED strip configuration:
LED_COUNT      = FLOOR_X * FLOOR_Y      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

na = np2DCharArr((FLOOR_X,FLOOR_Y))

for i in range(4):
  na.fillRow(i*4, 'P')
  na.fillCol(i*4, 'P')

na.clearScr()
na.print()
weaveCh = na.genColWeave()
weaveCo = na.mapColorStr2Int(weaveCh)
print("\n" + weaveCh)
print("\n" + str(weaveCo))

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

while True:
    ledRun(strip,weaveCo)

### end ###
