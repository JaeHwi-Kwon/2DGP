from pico2d import *
import random

#Object class
class Boy:
    pass
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