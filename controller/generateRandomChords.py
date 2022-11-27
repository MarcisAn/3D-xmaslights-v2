import random

for i in range(0,200):
    print("{r:%a, g:%a, b:%a}," % (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))