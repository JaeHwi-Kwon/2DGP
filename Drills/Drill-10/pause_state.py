import game_framework
from pico2d import *

import title_state
import main_state

name = 'PauseState'
image = None
button_state = True
button_timer = 0.0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def resume(): pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    global button_state
    global button_timer
    if(button_timer > 1.0):
        button_timer = 0
        if button_state == True: button_state = False
        elif button_state == False : button_state = True
    delay(0.01)
    button_timer += 0.05


def draw():
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if button_state == True:
        image.draw(400,300)
    update_canvas()
