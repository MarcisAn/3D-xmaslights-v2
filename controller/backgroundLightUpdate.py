import time
from animations.flicker import flicker
from animations.axis import axis
from animations.updown import updown

currentAnim = "axis"

def changeAnim(newanim,sio):
    global currentAnim
    currentAnim = newanim
    while currentAnim == "flicker":
        flicker(sio)
    while currentAnim == "axis":
        axis(sio)
    while currentAnim == "updown":
        updown()



def startLights():
    pass
    ##global anim_thread
    ##anim_thread = multiprocessing.Process(target=axis, name="Lights")
    ##anim_thread.start()
    ###while True:


if __name__ == '__backgroundLightUpdate__':
    startLights()