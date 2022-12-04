import sys
import time
import json
import math
from main import changeLight, updateLights

chords = json.load(open("L://Dev/xmaslights-v2/chords.json"))

def terminate():
    sys.exit()

def flicker():
    print("flicker")
    time.sleep(2)
    for i in range(0,199):
        changeLight(i, (0, 255, 0))
    updateLights()
    time.sleep(2)
    for i in range(0, 199):
        changeLight(i, (255, 0, 255))
    updateLights()