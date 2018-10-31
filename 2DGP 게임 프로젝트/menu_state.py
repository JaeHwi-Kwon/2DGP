import random
import json
import os

from pico2d import *
import game_framework
import game_world
import main_state


name = "MenuState"

menu = None

def enter():
    global menu
    menu = load_image('menu.png')

def exit():
    global menu
    del(menu)


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.push_state(main_state)


def update():
    pass


def draw():
    clear_canvas()
    menu.draw(1920//2, 1080//2)
    update_canvas()