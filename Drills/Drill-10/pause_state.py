import game_framework
from pico2d import *

name = 'PauseState'
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def resume():
    pass


def handle_events():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
