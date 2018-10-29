from pico2d import *

# John Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, IDLE_UP, RUN_UP = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): IDLE_UP,
    (RIGHT_DOWN, SDL_KEYUP, SDLK_UP): RUN_UP,
    (LEFT_DOWN, SDL_KEYUP, SDLK_UP): RUN_UP
}

gravity = 0.3

# John States

class IdleState:

    @staticmethod
    def enter(John, event):
        if event == RIGHT_DOWN:
            John.velocity += 1
        elif event == LEFT_DOWN:
            John.velocity -= 1
        elif event == RIGHT_UP:
            John.velocity -= 1
        elif event == LEFT_UP:
            John.velocity += 1
        John.timer = 300

    @staticmethod
    def exit(John, event):
        # fill here
        pass

    @staticmethod
    def do(John):
        John.frame = (John.frame + 1) % 8
        John.y += John.jump
        John.y = clamp(90, John.y, 800)
        John.jump -= gravity
        # fill here

    @staticmethod
    def draw(John):
        if John.dir == 1:
            John.image.clip_draw(John.frame * 100, 300, 100, 100, John.x, John.y)
        else:
            John.image.clip_draw(John.frame * 100, 200, 100, 100, John.x, John.y)


class RunState:

    @staticmethod
    def enter(John, event):
        if event == RIGHT_DOWN:
            John.velocity += 1
        elif event == LEFT_DOWN:
            John.velocity -= 1
        elif event == RIGHT_UP:
            John.velocity -= 1
        elif event == LEFT_UP:
            John.velocity += 1
        John.dir = John.velocity

    @staticmethod
    def exit(John, event):
        pass

    @staticmethod
    def do(John):
        John.frame = (John.frame + 1) % 8
        John.timer -= 1
        John.x += John.velocity
        John.x = clamp(25, John.x, 1600 - 25)
        John.y += John.jump
        John.y = clamp(90, John.y, 800)
        John.jump -= gravity


    @staticmethod
    def draw(John):
        if John.velocity == 1:
            John.image.clip_draw(John.frame * 100, 100, 100, 100, John.x, John.y)
        else:
            John.image.clip_draw(John.frame * 100, 0, 100, 100, John.x, John.y)


class JumpState:

    @staticmethod
    def enter(John, event):
        if event == RIGHT_DOWN:
            John.velocity += 1
        elif event == LEFT_DOWN:
            John.velocity -= 1
        elif event == RIGHT_UP:
            John.velocity -= 1
        elif event == LEFT_UP:
            John.velocity += 1
        John.dir = John.velocity
        John.jump = 10
        pass

    @staticmethod
    def exit(John, event):
        pass

    @staticmethod
    def do(John):
        John.frame = (John.frame + 1) % 8
        John.timer -= 1
        John.x += John.velocity
        John.x = clamp(25, John.x, 1600 - 25)
        John.y += John.jump
        John.y = clamp(90, John.y, 800)
        John.jump -= gravity
        pass

    @staticmethod
    def draw(John):
        if John.velocity == 1:
            John.image.clip_draw(John.frame * 100, 100, 100, 100, John.x, John.y)
        else:
            John.image.clip_draw(John.frame * 100, 0, 100, 100, John.x, John.y)
        pass


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: JumpState,
                IDLE_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               UP_DOWN: JumpState, RUN_UP: RunState},
    JumpState: {RUN_UP: RunState, IDLE_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState}
}

class John:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.jump = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

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

