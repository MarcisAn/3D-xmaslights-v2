import sys
import time
import json
import math
from main import changeLight, updateLights
import os

dirname = os.path.dirname(__file__)
chords = json.load(open(os.path.join(dirname, '../../chords.json')))

def terminate():
    sys.exit()

def flicker():
    time.sleep(0.5)
    for i in range(0,199):
        changeLight(i, (0, 255, 0))
    updateLights()
    time.sleep(0.5)
    for i in range(0, 199):
        changeLight(i, (255, 0, 255))
    updateLights()