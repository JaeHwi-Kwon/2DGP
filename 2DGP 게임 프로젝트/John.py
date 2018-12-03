import game_framework
from pico2d import *
import Sound


# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 100.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 16

# John Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, UP_UP = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP
}

gravity = 0.03


# John States
class IdleState:

    @staticmethod
    def enter(John, event):
        if event == RIGHT_DOWN:
            John.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            John.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            John.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            John.velocity += RUN_SPEED_PPS
        elif event == UP_DOWN:
            if John.y2 == John.y:
                Sound.play_sound_effect(2)
                John.jump = 4.0
                John.y = John.y2
        elif event == UP_UP:
            if John.jump > 0.0:
                John.jump = 0.0

    @staticmethod
    def exit(John, event):
        pass

    @staticmethod
    def do(John):
        John.y2 = John.y
        John.frame = (John.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 8
        John.y += John.jump
        John.jump -= gravity
        John.jump = clamp(-30.0, John.jump, 4.0)
        Sound.sets_sound_volume(Sound.sound_effect, 1, 0)


        John.x = clamp(0,John.x,John.bg.w)






    @staticmethod
    def draw(John):
        cx = John.x - John.bg.window_left
        John.image[int(John.frame)].draw(cx, John.y)


class RunState:

    @staticmethod
    def enter(John, event):
        if event == RIGHT_DOWN:
            John.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            John.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            John.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            John.velocity += RUN_SPEED_PPS
        elif event == UP_DOWN:
            if John.y2 == John.y:
                Sound.play_sound_effect(2)
                John.y = John.y2
                John.jump = 4.0
        elif event == UP_UP:
            if John.jump > 0.0:
                John.jump = 0.0
        John.dir = John.velocity
        John.dir = clamp(-1, John.velocity, 1)

    @staticmethod
    def exit(John, event):
        pass

    @staticmethod
    def do(John):
        John.y2 = John.y
        John.x2 = John.x
        John.frame = (John.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 8
        John.x += John.velocity * game_framework.frame_time
        John.y += John.jump
        John.jump -= gravity
        John.jump = clamp(-30.0, John.jump, 4.0)
        Sound.sets_sound_volume(Sound.sound_effect, 1, 80)

        John.x = clamp(0, John.x, John.bg.w)

    @staticmethod
    def draw(John):
        cx = John.x - John.bg.window_left
        if John.dir == 1:
            John.image[int(John.frame) + 8].draw(cx, John.y)
        else:
            John.image[int(John.frame) + 16].draw(cx, John.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: IdleState,
                UP_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: RunState,
               UP_UP: RunState}
}


class John:

    def __init__(self):
        Sound.init()
        Sound.repeated_play_sound_effect(1)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x, self.y = 100, 300
        self.x2, self.y2 = 100, 300
        self.image = [load_image('./Image/main_stage/John/john %d.png' % i) for i in range(1, 25)]
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.jump = 0
        self.jump_toggle = True
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def get_bb(self):
        return self.x - 18, self.y - 60, self.x + 18, self.y + 18

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def back_to_the_position_before_x(self):
        self.x = self.x2

    def back_to_the_position_before_y(self):
        self.y = self.y2
        self.jump = 0

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
