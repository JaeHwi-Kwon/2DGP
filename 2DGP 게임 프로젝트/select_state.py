from pico2d import *
import game_framework
import game_world
import selection

from main_menu import Whitescreen
from main_menu import Stage_Select
from main_menu import Stage_Select_Back
import world_build_state
import menu_state
import Sound

FIRST, SECOND, THIRD, FOURTH = 1, 2, 3, 4

name = "SelectState"

stage_select_back = None
stage_select = None
white = None

def enter():

    global white
    white = Whitescreen()
    game_world.add_object(white, 0)

    global stage_select_back
    stage_select_back = Stage_Select_Back()
    game_world.add_object(stage_select_back, 0)

    global stage_select
    stage_select = Stage_Select()
    game_world.add_object(stage_select, 0)
    selection = 0


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Sound.play_sound_effect(0)
            stage_select.selected -= 1
            selection.selection_decrease()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Sound.play_sound_effect(0)
            stage_select.selected += 1
            selection.selection_increase()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(menu_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            Sound.play_sound_effect(0)
            game_framework.change_state(world_build_state)

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
