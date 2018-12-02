from pico2d import *
import game_framework
import random
import world_build_state

LEFT, RIGHT = -1, 1

class Block:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('./Image/main_stage/BLOCK_BASIC.png')

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

    #def set_center_object(self, john):
    #    pass


class Enemy:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = [load_image('./Image/main_stage/Enemy/monster %d.png' % i) for i in range(1, 8)]
        self.frame = random.randint(0, 7)

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)
        pass

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 7
        pass


class Cannon:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = [load_image('./Image/main_stage/Cannon/cannon %d.png' % i) for i in range(1, 4)]
        self.frame = random.randint(1, 4)
        self.dir = LEFT

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)
        pass

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 3


class Trap:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = [load_image('./Image/main_stage/Trap/trap %d.png' % i) for i in range(1, 4)]
        self.frame = 1

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def draw(self):
        self.image[int(self.frame)].draw(self.x, self.y)
        pass

    def update(self):
        self.frame = (self.frame + game_framework.frame_time*10) % 3


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
