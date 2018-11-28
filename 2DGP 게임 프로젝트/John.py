import game_framework
from pico2d import *


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
FRAMES_PER_ACTION = 8

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


def blk(y, x):
    # left,up,right,down
    return 120*x, 1080-120*y, 120*(x+1), 960 - 120*y


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
                John.jump = 4.0
        elif event == UP_UP:
            if John.jump > 0.0:
                John.jump = 0.0

    @staticmethod
    def exit(John, event):
        # fill here
        pass

    @staticmethod
    def do(John):
        John.y2 = John.y
        John.frame = (John.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 8
        John.y += John.jump
        John.jump -= gravity
        John.jump = clamp(-30.0, John.jump, 4.0)
        John.left, John.up, John.right, John.down = John.x - 15, John.y + 30, John.x + 15, John.y - 30






    @staticmethod
    def draw(John):
        if John.dir == 1:
            John.image.clip_draw(int(John.frame) * 100, 300, 100, 100, John.x, John.y)
        else:
            John.image.clip_draw(int(John.frame) * 100, 200, 100, 100, John.x, John.y)


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
        John.x = clamp(25, John.x, 1920 - 25)
        John.y += John.jump
        John.jump -= gravity
        John.jump = clamp(-30.0, John.jump, 4.0)
        John.left, John.up, John.right, John.down = John.x - 15, John.y + 30, John.x + 15, John.y - 30



    @staticmethod
    def draw(John):
        if John.dir == 1:
            John.image.clip_draw(int(John.frame) * 100, 100, 100, 100, John.x, John.y)
        else:
            John.image.clip_draw(int(John.frame) * 100, 0, 100, 100, John.x, John.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: IdleState,
                UP_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: RunState,
               UP_UP: RunState}
}


class John:

    def __init__(self):
        self.x, self.y = 100, 300
        self.x2, self.y2 = 100, 300
        self.left, self.up, self.right, self.down = self.x - 15, self.y + 30, self.x +15, self.y - 30
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.jump = 0
        self.jump_toggle = True
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 15, self.y - 30, self.x + 15, self.y + 30

    def add_event(self, event):
        self.event_que.insert(0, event)

    def back_to_the_position_before(self):
        self.x = self.x2
        self.y = self.y2

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)