from pico2d import*
import random
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_by_line(p1,p2):
    pass



open_canvas()
size = 20
points = [(random.randint(-350,350),random.randint(-250,250)) for i in range(size)]
n=1
while True:
    move_by_line(points[n-1],points[n])
    n=(n+1)%size
    pass

close_canvas()