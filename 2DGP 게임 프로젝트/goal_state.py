from pico2d import *
import game_framework
import menu_state
import Sound
import game_framework

name = "GoalState"

goal = None


def enter():
    global goal
    goal = load_image('goal_state.png')
    Sound.init()
    Sound.play_background_sound(1)
    Sound.sets_sound_volume(Sound.sound_effect, 1, 0)


def exit():
    global goal
    del(goal)


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
    goal.draw(1920//2, 1080//2)
    update_canvas()
