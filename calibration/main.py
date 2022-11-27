import time
import pygame
import sys
import serial

pygame.init()
screen = pygame.display.set_mode((1800, 300))
pygame.display.set_caption("Lampiņas")


ser=serial.Serial("COM5")

cords = []
lightCount = 5

xAxis = []
yAxis = []
zAxis = []

axis = "x"

while True:
    input = ser.readline().decode()
    if "button" in input.strip():
        lightIndex = input.strip()[7:]
        print(lightIndex)
        if axis == "x":
            xAxis.append(cord)
        if axis == "y":
            yAxis.append(cord)
        if axis == "z":
            zAxis.append(cord)
        if len(xAxis) == lightCount:
            print("pēdējā lampiņa")
            if axis == "x":
                axis == "y"
            if axis == "y":
                axis == "z"
            if axis == "z":
                print("kalibrēšana pabeigta")

    else:
        x = int(input)*2
        #x = input+450*2
        cord = x/2-450
    pygame.Surface.fill(screen, (0, 0, 0, 0))
    pygame.draw.rect(screen, "white", (x, 1, 10, 100))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
