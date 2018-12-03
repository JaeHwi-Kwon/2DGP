import game_framework
import pico2d
import menu_state

pico2d.open_canvas(1920, 1080, True)
game_framework.run(menu_state)
pico2d.close_canvas()
