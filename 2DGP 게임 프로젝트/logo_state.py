from pico2d import *
import game_framework
import menu_state

import game_framework

name = "LogoState"

logo1 = None
blkscreen = None
logo_time = None
opacity = 1.0
opac_spd = 0.0
delta_opac = 0.001

def enter():
    global logo_time
    global logo1
    global blkscreen
    logo1 = load_image('logo.png')
    blkscreen = load_image('black_screen.png')
    logo_time = get_time()

def exit():
    global logo_time
    del(logo_time)


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


def update():
    global blkscreen
    global opacity
    global delta_opac, opac_spd
    opac_spd += delta_opac
    opacity -= opac_spd*game_framework.frame_time
    opacity = clamp(0.0,opacity,1.0)
    blkscreen.opacify(opacity)
    if opacity <= 0.0:
        delay(2.0)
        opac_spd = 0
        delta_opac = - delta_opac
    global logo_time
    if get_time() - logo_time > 7:
        game_framework.change_state(menu_state)


def draw():
    clear_canvas()
    logo1.draw(1920//2, 1080//2)
    blkscreen.draw(1920//2, 1080//2)
    update_canvas()
