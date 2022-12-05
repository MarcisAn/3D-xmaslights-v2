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

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def updownsphere(sio):
    global level
    time.sleep(0.05)
    level += 0.05
    index = 0
    for light in chords:
        center = math.sin(level)
        center = center*450
        if distance(0,0,center,light["x"],light["y"], light["z"]) > 100:
            changeLight(index, (0, 0, 0))
        else:
            changeLight(index, (255, 0, 0))
        index += 1
    updateLights(sio)