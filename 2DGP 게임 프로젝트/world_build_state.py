import random
import json
import pickle
import os

from pico2d import *
import game_framework
import main_state
import game_world

import main_state

from John import John
from load_map import Block
from load_map import Enemy
from load_map import Cannon
from load_map import Goal
from load_map import Trap
from background import Background

back = None
john = None
block = None
enemy = None
cannon = None
goal = None
trap = None

blocks = []
enemies = []
cannons = []
traps = []
goals = []

BLANK, BLOCK, ENEMY, CANNON, TRAP, GOAL = range(6)
BLOCK_WIDTH = 120
BLOCK_HEIGHT = 120

name = "WorldBuildState"

menu = None


def enter():

    global back
    back = Background()
    game_world.add_object(back, 0)

    global john
    john = John()
    game_world.add_object(john, 1)

    with open('first_stage_data.json', 'r') as f:
        stage_data_list = json.load(f)

    for i in range(stage_data_list[0][0]):
        for j in range(stage_data_list[0][1]):
            if stage_data_list[1][i][j] == BLOCK:
                block = Block(60 + 120 * j, 1020 - 120 * i)
                blocks.append(Block(60 + 120 * j, 1020 - 120 * i))
                game_world.add_object(block, 1)
                pass
            elif stage_data_list[1][i][j] == CANNON:
                cannon = Cannon(60 + 120 * j, 1020 - 120 * i)
                cannons.append(Cannon(60 + 120 * j, 1020 - 120 * i))
                game_world.add_object(cannon, 1)
                pass
            elif stage_data_list[1][i][j] == ENEMY:
                enemy = Enemy(60 + 120 * j, 1020 - 120 * i)
                enemies.append(Enemy(60 + 120 * j, 1020 - 120 * i))
                game_world.add_object(enemy, 2)
                pass
            elif stage_data_list[1][i][j] == TRAP:
                trap = Trap(60 + 120 * j, 1020 - 120 * i)
                traps.append(Trap(60 + 120 * j, 1020 - 120 * i))
                game_world.add_object(trap, 2)
                pass
            elif stage_data_list[1][i][j] == GOAL:
                goal = Goal(60 + 120 * j, 1020 - 120 * i)
                goals.append(Goal(60 + 120 * j, 1020 - 120 * i))
                game_world.add_object(goal, 3)
            else:
                pass

    game_framework.change_state(main_state)

def exit():
    pass


def pause():
    pass


def resume():
    pass


def get_john():
    return john


def get_objects():
    return blocks, cannons, enemies, traps, goals

def get_world_size():
    with open('first_stage_data.json', 'r') as f:
        stage_data_list = json.load(f)
    return stage_data_list[0][0] * BLOCK_WIDTH, stage_data_list[0][1] * BLOCK_HEIGHT


def create_new_world():
    pass


def load_saved_world():
    pass


def handle_events():
    pass


def update():
    pass


def draw():
    pass
