import random
import json
import os

from pico2d import *
import game_framework
import game_world
import select_state
import world_build_state

name = "MenuState"

menu = None
select = None
blackscreen = None

opac_spd = 0.0
delta_opac = 0.8
frame = 0
BASED__MENU_X_POSITION = 1920/4

PLAY, LOAD, QUIT = 1, 2, 3

def enter():
    global select
    select = Select()
    global blackscreen
    blackscreen = Blackscreen()
    global menu
    menu = [load_image("./Image/Title_Image/Title_%d.png" % i) for i in range(1, 6)]

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
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            select.selected -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            select.selected += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            if select.selected == PLAY:
                game_framework.push_state(world_build_state)
            elif select.selected == LOAD:
                game_framework.push_state(select_state)
            elif select.selecte == QUIT:
                game_framework.quit()



def update():
    global frame
    frame = (frame + game_framework.frame_time*10) % 5
    select.update()
    blackscreen.update()
    pass


def draw():
    global frame
    clear_canvas()
    menu[int(frame)].draw(1920//2, 1080//2)
    select.draw()
    blackscreen.draw()
    update_canvas()

class Select:
    pen_image = None
    select_image = None
    def __init__(self):
        self.pen_image = [load_image('./Image/Title_Image/Title_Pen_%d.png' % i) for i in range(1, 4)]
        self.select_image = [load_image('./Image/Title_Image/Title_Select_%d.png' % i) for i in range(1, 4)]
        self.frame = 0
        self.pen_x, self.pen_y = BASED__MENU_X_POSITION, 1080 / 3
        self.select_x, self.select_y = 1920/2, 1080/4
        self.selected = 1

    def draw(self):
        self.pen_image[int(self.frame)].draw(self.pen_x, self.pen_y)
        self.select_image[int(self.frame)].draw(self.select_x, self.select_y)

    def update(self):
        self.selected = clamp(1, self.selected, 3)
        self.pen_x = BASED__MENU_X_POSITION*self.selected
        self.frame = (self.frame + game_framework.frame_time*10) % 3

class Blackscreen:
    def __init__(self):
        self.image = load_image('./Image/Title_Image/black_screen.png')
        self.x, self.y = 1920/2, 1080/2
        self.opacity = 1.0

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.opacify(self.opacity)

    def update(self):
        if self.opacity:
            self.opacity -= game_framework.frame_time*delta_opac
        self.opacity = clamp(0.0, self.opacity, 1.0)