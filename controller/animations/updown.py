import sys
import time
import json
import math
from main import changeLight, updateLights

chords = json.load(open("L://Dev/xmaslights-v2/chords.json"))

level = 0.0


def mod(i):
    if i <0:
        return 0-i
    else:
        return i
def updown():
    global level
    while True:
        time.sleep(0.3)
        #print(math.sin(level))
        level += 50
        for index in range(0,199):
            if mod(math.sin(level) + 0.5 - chords[index]["z"]) < 100:
                changeLight(index, (0, 0, 0))
            else:
                changeLight(index, (0, 255, 0))
        updateLights()