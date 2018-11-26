import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state as start_state

from boy import Boy
from zombie import Zombie


boy = None


name = "rank_state"

menu = None

def enter():
    global menu
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

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
                game_framework.change_state(start_state)

def update():
    pass

def draw():
    clear_canvas()
    update_canvas()