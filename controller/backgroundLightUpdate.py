import time
from animations.flicker import flicker
from animations.axis import axis
from animations.updown import updown
from animations.updownsphere import updownsphere

currentAnim = "axis"

def changeAnim(newanim):
    global currentAnim
    currentAnim = newanim
    while currentAnim == "flicker":
        print("flicker")
        flicker()
    while currentAnim == "axis":
        print("axis")
        axis()
    while currentAnim == "updown":
        print("updown")
        updown()
    while currentAnim == "updownsphere":
        print("updownsphere")
        updownsphere()