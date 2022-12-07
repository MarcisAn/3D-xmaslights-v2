import time
import requests
import socketio
from sys import platform
import json
from backgroundLightUpdate import *
import os
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 200      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

if platform == "linux" or platform == "linux2":
    import board
    import neopixel
    pixels = neopixel.NeoPixel(board.D18,200)
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

if platform == "linux" or platform == "linux2":
    debug = True
elif platform == "win32":
    debug = False

#debug = True
retryTime = 10

dirname = os.path.dirname(__file__)
telegramData = json.load(open(os.path.join(dirname, '../telegram.json')))

# standard Python
sio = socketio.Client()

state = []
buffer = []


for i in range(0,200):
    state.append((0,0,0))

def changeLight(index, color):
    if platform == "linux" or platform == "linux2":
        strip.setPixelColor(index, Color(int(color[1]*254), int(color[0]*254), int(color[2]*254)))
        #pixels[index] = color
    buffer.append([index,(color)])

def updateLights(sio_new):
    sio_new.emit("lightUpdate", buffer)
    if platform == "linux" or platform == "linux2":
        strip.show()
    for l in buffer:
        state[l[0]] = l[1]
    f = open("lightData.json", "w")
    #f.write(json.dumps(state))
    #print(state)

    for i in state:
        f.write(str(i[0])+" "+ str(i[1])+ " "+str(i[2])+"\n")
    f.close()
    buffer.clear()


def sendMessage(text):
    if debug:
        url = "https://api.telegram.org/bot" + telegramData["key"] + "/sendMessage?chat_id=" + \
              telegramData["id"] + \
              "&text=" + text
        requests.get(url)

@sio.event
def message(data):
    print('I received a message!')


@sio.on('lightControll')
def on_message(data):
    changeAnim(data, sio)


@sio.on('*')
def catch_all(event, data):
     pass


@sio.event
def connect():
    print("savienojums izveidots")
    sendMessage("kontrolieris pievienojies")
    changeAnim("axis",sio)


@sio.event
def connect_error(data):
    print("savienojums neizdevās")
    print(data)
    sendMessage("kontroliera savienojums neizdevās")


@sio.event
def disconnect():
    print("kontrolieris atvienojies")
    sendMessage("kontrolieris atvienojies")


def connect():
    try:
        if platform == "linux" or platform == "linux2":
            sio.connect('wss://lampinas.cvgmerch.lv')
        elif platform == "win32":
            sio.connect('ws://localhost:3000', namespaces=["/"])
        #sio.connect('wss://lampinas.cvgmerch.lv')
        return True
    except Exception as err:
        print(err)
        sendMessage("kontrolera savienojums neizdevās, mēģinām pēc "+str(retryTime))
        print("neizdevās savienoties")
        return False

if __name__ == '__main__':
    while sio.connected == False:
        connect()
        time.sleep(retryTime)
    
