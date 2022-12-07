import json
import math
import time
from main import changeLight, updateLights
import os

dirname = os.path.dirname(__file__)
chords = json.load(open(os.path.join(dirname, '../../chords.json')))


level = -1.0


def mod(i):
    if i <0:
        return 0-i
    else:
        return i
def axis(sio):
    global level
    while level<1:
        time.sleep(0.05)
        level += 0.05
        index = 0
        for light in chords:
            pass
            if mod(math.sin(level) * 450 + 0.5 - light["x"]) < 70:
                changeLight(index, (1, 0, 0))
            else:
                changeLight(index, (0, 0, 0))
            index += 1
        updateLights(sio)
    level = -1.0
    while level<1:
        time.sleep(0.05)
        level += 0.05
        index = 0
        for light in chords:
            pass
            if mod(math.sin(level) * 450 + 0.5 - light["y"]) < 70:
                changeLight(index, (0, 1, 0))
            else:
                changeLight(index, (0, 0, 0))
            index += 1
        updateLights(sio)
    level = -1.0
    while level<1:
        time.sleep(0.05)
        level += 0.05
        index = 0
        for light in chords:
            pass
            if mod(math.sin(level) * 450 + 0.5 - light["z"]) < 70:
                changeLight(index, (0, 0, 1))
            else:
                changeLight(index, (0, 0, 0))
            index += 1
        updateLights(sio)
    level = -1.0
