from pico2d import*
import random

KPU_WIDTH,KPU_HEIGHT = 1280,1024
open_canvas(KPU_WIDTH,KPU_HEIGHT)
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
background = load_image('KPU_GROUND.png')

def move_by_line(p1,p2):
    frame = 0
    x,y=p1[0],p1[1]
    if p1[0]>p2[0]:
        des = 0
    elif p1[0]<=p2[0]:
        des=100
    for i in range(1,100,2):
        t=i/100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        clear_canvas()
        background.draw(KPU_WIDTH//2,KPU_HEIGHT//2)
        character.clip_draw((int)(frame) * 100, des, 100, 100, x, y)
        update_canvas()
        frame = (frame+1)%8
        delay(0.01)
        get_events()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running = False


size = 20
points = [(random.randint(50,1230),random.randint(50,974)) for i in range(size)]
size=len(points)
n=1
running = True
while running:
    move_by_line(points[n-1],points[n])
    n=(n+1)%size
    handle_events()

close_canvas()