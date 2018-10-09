from pico2d import *
import random

#Object class
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90

class Ball:
    pass
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

#Initialization
open_canvas()
running=True

#Main loop
while running:
    pass

#Finalization
close_canvas()