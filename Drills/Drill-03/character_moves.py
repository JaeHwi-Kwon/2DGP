from pico2d import*
import math

open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')

def rect_mov():
    x=400
    while x<800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.005)

    y=90
    while y<600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        delay(0.005)
    
    while x>0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.005)

    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.005)

    while x<400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.005)

def circle_mov():
    pi=3.14
    r=pi*3/2
    while r<pi*7/2:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(210*(math.cos(r))-0*(math.sin(r))+400,210*(math.sin(r))+0*(math.cos(r))+300)
        r=r+pi/180
        delay(0.01)

while True:
    rect_mov()
    circle_mov()
