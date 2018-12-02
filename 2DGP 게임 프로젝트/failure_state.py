from pico2d import *
import game_framework
import menu_state

import game_framework

name = "FailureState"

failure = None

def enter():
    global failure
    failure = load_image('failure_state.png')

def exit():
    global failure
    del(failure)


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
            game_framework.change_state(menu_state)


def update():
    pass


def draw():
    clear_canvas()
    failure.draw(1920//2, 1080//2)
    update_canvas()
