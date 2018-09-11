from pico2d import*
import math

open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')

def rect_mov():
    x=400
    while x<800:
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,90)
        update_canvas()
        x=x+2
        delay(0.005)
        get_events()

    y=90
    while y<600:
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
        y=y+2
        delay(0.005)
        get_events()
    
    while x>0:
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
        x=x-2
        delay(0.005)
        get_events()

    while y>90:
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
        y=y-2
        delay(0.005)
        get_events()

    while x<400:
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,90)
        update_canvas()
        x=x+2
        delay(0.005)
        get_events()

def circle_mov():
    pi=3.14
    r=pi*3/2
    while r<pi*7/2:
        clear_canvas()
        grass.draw(400,30)
        character.draw(210*(math.cos(r))-0*(math.sin(r))+400,210*(math.sin(r))+0*(math.cos(r))+300)
        update_canvas()
        r=r+pi/180
        delay(0.01)
        get_events()

while True:
    rect_mov()
    circle_mov()
