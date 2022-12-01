import time
import requests
import socketio
from sys import platform
import json

if platform == "linux" or platform == "linux2":
    debug = True
elif platform == "win32":
    debug = False

#debug = True
retryTime = 10

telegramData = json.load(open("../telegram.json"))
# standard Python
sio = socketio.Client()

def sendMessage(text):
    if debug:
        url = "https://api.telegram.org/bot" + telegramData["key"] + "/sendMessage?chat_id=" + \
              telegramData["id"] + \
              "&text=" + text
        requests.get(url)

@sio.event
def message(data):
    print('I received a message!')


@sio.on('my message')
def on_message(data):
    print('I received a message!')


@sio.on('*')
def catch_all(event, data):
    pass


@sio.event
def connect():
    print("savienojums izveidots")
    sendMessage("kontrolieris pievienojies")
    sio.emit("connectioninfo", "controller")


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
        sio.connect('https://lampinas.cvgmerch.lv')
        return True
    except Exception as err:
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

tryConnecting()

# time.sleep(1)
# sio.emit('data', {'foo': 'bar'})
