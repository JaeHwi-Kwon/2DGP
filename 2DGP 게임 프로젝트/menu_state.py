from pico2d import *
import game_framework
import game_world

from main_menu import Select
from main_menu import Blackscreen
from main_menu import Menu
import select_state
import world_build_state
import Sound

PLAY, LOAD, QUIT = 1, 2, 3

name = "MenuState"

menu = None
select = None
black = None
black_back = None


def enter():
    global menu
    menu = Menu()
    game_world.add_object(menu, 0)

    global select
    select = Select()
    game_world.add_object(select, 0)

    global black
    black = Blackscreen()
    game_world.add_object(black, 0)

    global black_back
    black_back = load_image('./Image/main_stage/Background/background.png')

    #Sound.init()
    #Sound.play_background_sound(2)
    #Sound.sets_sound_volume(Sound.background_sound, 2, 80)


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
            select.selected -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Sound.play_sound_effect(0)
            select.selected += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            Sound.play_sound_effect(0)
            if select.selected == PLAY:
                game_framework.change_state(world_build_state)
            elif select.selected == LOAD:
                game_framework.change_state(select_state)
            elif select.selected == QUIT:
                game_framework.quit()


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    pass


def draw():
    clear_canvas()
    global black_back
    black_back.draw(1920*3/2, 1080/2)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
