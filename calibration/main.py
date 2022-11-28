import time
import pygame
import sys
import serial

pygame.init()
screen = pygame.display.set_mode((1800, 300))
pygame.display.set_caption("Lampiņas")

if sys.platform == "darwin":
    ser = serial.Serial("/dev/cu.usbmodem411")
else:
    ser = serial.Serial("COM5",baudrate=9600)

cords = []
lightCount = 5

xAxis = []
yAxis = []
zAxis = []

axis = []
input = ""
while True:
    if ser.inWaiting()>0:
        input = ser.readline().decode()
        print(input)
    #input = "1"
    if "button" in input.strip():
        lightIndex = input.strip()[7:]
        print(lightIndex, cord)
        axis.append(cord)
        if len(axis) == lightCount:
            print("kalibrēšana pabeigta")
            break

    else:
        try:
            x = int(input)*2
            cord = x / 2 - 450
        except:
            pass


    pygame.Surface.fill(screen, (0, 0, 0, 0))
    try:
        pygame.draw.rect(screen, "white", (x, 1, 10, 100))
    except:
        pass
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

for i in axis:
    print(round(i), end=" ")