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

    def draw(self):
        self.image.draw(self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(10, 790), random.randint(310, 590)
        self.image = load_image('ball21x21.png')
        self.velocity = random.randint(1, 8)

    def draw(self):
        self.image.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# Initialization
open_canvas()
grass = Grass()
team = [Boy() for i in range(11)]
rand_ball = random.randint(1, 19)
B_ball = [BigBall() for i in range(rand_ball)]
S_ball = [SmallBall() for i in range(20-rand_ball)]
running = True

# Main loop
while running:
    handle_events()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for bigball in B_ball:
        bigball.draw()
    for smallball in S_ball:
        smallball.draw()
    update_canvas()
    delay(0.05)

# Finalization
close_canvas()