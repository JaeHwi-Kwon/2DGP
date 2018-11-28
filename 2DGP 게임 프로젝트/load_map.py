from pico2d import *
import game_framework
import random
import world_build_state


class Block:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('block_normal.png')

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

    def update(self):
        pass


class Enemy:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('block_normal.png')

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

    def update(self):
        pass


class Cannon:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('cannon.png')

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

    def update(self):
        pass


class Trap:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('trap.png')

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

    def update(self):
        pass


class Goal:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('goal.png')

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

    def update(self):
        pass
