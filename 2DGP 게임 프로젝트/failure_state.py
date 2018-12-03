from pico2d import *
import game_world
import world_build_state
import Sound
import game_framework

name = "FailureState"

failure = None

def enter():
    global failure
    failure = Failure_State()
    game_world.add_object(failure, 0)

    Sound.init()
    Sound.play_sound_effect(3)
    Sound.sets_sound_volume(Sound.sound_effect, 1, 0)

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_state(world_build_state)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

class Failure_State:
    def __init__(self):
        self.image = [load_image('./Image/Title_Image/failure %d.png' % i) for i in range(1, 4)]
        self.x, self.y = get_canvas_width()/2, get_canvas_height()/2
        self.frame = 0

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 3
