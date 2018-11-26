import game_framework
import pico2d

import logo_state
import main_state

pico2d.open_canvas(1920, 1080)
game_framework.run(main_state)
pico2d.close_canvas()