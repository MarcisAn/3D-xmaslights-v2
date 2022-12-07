import sys
import time
import json
import math
from main import changeLight, updateLights
import os

dirname = os.path.dirname(__file__)
chords = json.load(open(os.path.join(dirname, '../../chords.json')))

level = 0.0


def mod(i):
    if i <0:
        return 0-i
    else:
        return i
def updown(sio):
    global level
    time.sleep(0.05)
    print(math.sin(level))
    level += 0.05
    index = 0
    for light in chords:
        if mod(math.sin(level)*450 + 0.5 - light["z"]) > 90:
            changeLight(index, (int(math.sin(level)), int(1-math.sin(level)), 0))
        else:
            changeLight(index, (0, 0, 255))
        index += 1
    updateLights(sio)
