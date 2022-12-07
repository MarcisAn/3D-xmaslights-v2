import time
import requests
import socketio
from sys import platform
import json
import os
import threading
from backgroundLightUpdate import *

# LED strip configuration:
LED_COUNT      = 200
LED_PIN        = 18
#LED_PIN        = 10
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 255
LED_INVERT     = False
LED_CHANNEL    = 0

if platform == "linux" or platform == "linux2":
    from rpi_ws281x import *
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

if platform == "linux" or platform == "linux2":
    debug = True
elif platform == "win32":
    debug = False

#debug = True

dirname = os.path.dirname(__file__)
telegramData = json.load(open(os.path.join(dirname, '../telegram.json')))


state = []
buffer = []

def fetchServer():
    while True:
        time.sleep(1)
        if platform == "linux" or platform == "linux2":
            url = "https://lampinas.cvgmerch.lv"
        elif platform == "win32":
            url = "http://localhost:3000"
        res = requests.get(url+"/currentAnim")
        print(res.headers)
        #changeAnim(res.json()["anim"])

for i in range(0,200):
    state.append((0,0,0))

def changeLight(index, color):
    if platform == "linux" or platform == "linux2":
        strip.setPixelColor(index, Color(int(color[1]*254), int(color[0]*254), int(color[2]*254)))
        #pixels[index] = color
    buffer.append([index,(color)])

def updateLights():
    if platform == "linux" or platform == "linux2":
        strip.show()
    for l in buffer:
        state[l[0]] = l[1]
    buffer.clear()


def sendMessage(text):
    if debug:
        url = "https://api.telegram.org/bot" + telegramData["key"] + "/sendMessage?chat_id=" + \
              telegramData["id"] + \
              "&text=" + text
        requests.get(url)

if __name__ == "__main__":
    thread = threading.Thread(target=fetchServer)
    thread.start()