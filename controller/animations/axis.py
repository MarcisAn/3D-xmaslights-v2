import time
from main import changeLight, updateLights

def axis(sio):
   print("axis")
   time.sleep(2)
   for i in range(0,199):
       changeLight(i, (0, 255, 0))
   updateLights(sio)
   time.sleep(2)
   for i in range(0, 199):
       changeLight(i, (0, 0, 255))
   updateLights(sio)