from pico2d import *
import random

# Object class
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1)%8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), random.randint(320, 580)
        self.image = load_image('ball41x41.png')
        self.velocity = random.randint(1, 8)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randing(10, 790), random.randint(310, 590)
        self.image = load_image('ball21xz21.png')
        self.velocity = random.randint(1, 8)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

# Initialization
open_canvas()
running=True

# Main loop
while running:
    pass

#Finalization
close_canvas()