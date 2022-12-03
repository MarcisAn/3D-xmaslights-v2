import time
import json
import math
from main import changeLight, updateLights

chords = json.load(open("L://Dev/xmaslights-v2/chords.json"))

level = 0.0
goingPos = True

def mod(i):
    if i <0:
        return 0-i
    else:
        return i

while True:
    time.sleep(0.03)
    print(math.sin(level))
    level += 0.1
    index = 0
    for light in chords:
        pass
        if mod(math.sin(level)+0.5 - light["z"]) < 0.1:
            changeLight(index, (255,0,0))
        else:
            changeLight(index, (0, 255, 0))
        index += 1
    updateLights()