import game_framework
import pico2d

import logo_state
import main_state
import menu_state
import world_build_state

pico2d.open_canvas(1920, 1080, True)
game_framework.run(world_build_state)
pico2d.close_canvas()
