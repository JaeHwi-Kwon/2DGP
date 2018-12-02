import random
import json
import os

from pico2d import *
import game_framework
import game_world
import menu_state
import world_build_state


name = "SelectState"

stage_img = None
stage = 0

def enter():
    global stage_img
    stage_img = load_image('stage.png')

def exit():
    global stage_img
    del(stage_img)


def pause():
    pass


def resume():
    pass


def handle_events():
    global stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(menu_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            stage += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            stage -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_state(world_build_state)
        stage = clamp(0, stage, 2)


def update():
    pass


def draw():
    clear_canvas()
    stage_img.draw(1920//2, 1080//2)
    update_canvas()