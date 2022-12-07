import json
import time
from sys import platform


if platform == "linux" or platform == "linux2":
    import board
    import neopixel
    pixels = neopixel.NeoPixel(board.D18,200)

while True:
    f = open("lightData.json", "r")
    data = f.read()
    data = data.split("\n")
    for j in data:
        pass
        #print(j)
    for i in range(0,199):
        if platform == "linux" or platform == "linux2":
            print(data[i])
            #pixels[i] = data[i]
    if platform == "linux" or platform == "linux2":
        pixels.show()
    time.sleep(1/20)
