import random
import json
import os

from pico2d import *
import game_framework

from John import John
from grass import Grass


name = "MainState"

john = None
grass = None

def enter():
    global john, grass
    john = John()
    grass = Grass()


def exit():
    global john, grass
    del john
    del grass

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            john.handle_event(event)


def update():
    john.update()


def draw():
    clear_canvas()
    grass.draw()
    john.draw()
    update_canvas()







