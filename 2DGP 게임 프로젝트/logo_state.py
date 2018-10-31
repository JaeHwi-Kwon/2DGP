from pico2d import *
import game_framework
import menu_state


name = "LogoState"

logo1 = None
logo_time = None

def enter():
    global logo_time
    global logo1
    logo1 = load_image('logo.png')
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
    global logo_time
    if get_time() - logo_time > 5:
        game_framework.change_state(menu_state)


def draw():
    clear_canvas()
    logo1.draw(1920//2, 1080//2)
    update_canvas()
