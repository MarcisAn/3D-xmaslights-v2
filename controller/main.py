import time
import requests
import socketio
from sys import platform
import json
from backgroundLightUpdate import *

if platform == "linux" or platform == "linux2":
    debug = True
elif platform == "win32":
    debug = False

#debug = True
retryTime = 10

telegramData = json.load(open("L:/Dev/xmaslights-v2/telegram.json"))

# standard Python
sio = socketio.Client()

state = []
buffer = []


for i in range(0,200):
    state.append((0,0,0))

def changeLight(index, color):
    buffer.append([index,(color)])

def updateLights(sio_new):
    print(sio_new.connection_namespaces)
    sio_new.emit("lightUpdate", buffer)
    for l in buffer:
        state[l[0]] = l[1]
    buffer.clear()


def sendMessage(text):
    if debug:
        url = "5https://api.telegram.org/bot" + telegramData["key"] + "/sendMessage?chat_id=" + \
              telegramData["id"] + \
              "&text=" + text
        requests.get(url)

@sio.event
def message(data):
    print('I received a message!')


@sio.on('lightControll')
def on_message(data):
    changeAnim(data)


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
        #if platform == "linux" or platform == "linux2":
        #    sio.connect('wss://lampinas.cvgmerch.lv')
        #elif platform == "win32":
        #    sio.connect('ws://localhost:3000', namespaces=["/"])
        sio.connect('wss://lampinas.cvgmerch.lv')
        return True
    except Exception as err:
        print(err)
        sendMessage("kontrolera savienojums neizdevās, mēģinām pēc "+str(retryTime))
        print("neizdevās savienoties")
        return False

def tryConnecting():
    while True:
        if connect() == False:
            connect()
            time.sleep(10)
        else:
            break


if __name__ == '__main__':
    tryConnecting()
