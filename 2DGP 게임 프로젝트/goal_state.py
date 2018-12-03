from pico2d import *
import select_state
import Sound
import game_framework
import game_world
import selection

name = "GoalState"

goal = None


def enter():
    global goal
    goal = Goal_State()
    game_world.add_object(goal, 0)
    selection.selection = 1
    Sound.init()
    Sound.play_background_sound(1)
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
            game_framework.change_state(select_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_state(select_state)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

class Goal_State:
    def __init__(self):
        self.image = [load_image('./Image/Title_Image/goal %d.png' % i) for i in range(1, 4)]
        self.x, self.y = get_canvas_width()/2, get_canvas_height()/2
        self.frame = 0

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 3