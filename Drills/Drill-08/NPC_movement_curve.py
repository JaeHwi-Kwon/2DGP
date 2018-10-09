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


def move_by_curve(list):
    global size
    frame = 0
    for i in range(0,10):
        x, y = list[i][0], list[i][1]
        if list[i][0] > list[(i+1)%size][0]:
            des = 0
        elif list[i][0] <= list[(i+1)%size][0]:
            des = 100
        for j in range(0,100,2):
            t=j/100
            x = ((-t ** 3 + 2 * t ** 2 - t) * list[i - 1][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * list[(i)][0] + (
                        -3 * t ** 3 + 4 * t ** 2 + t) * list[(i + 1)%size][0] + (t ** 3 - t ** 2) * list[(i + 2)%size][0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * list[i - 1][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * list[i][1] + (
                        -3 * t ** 3 + 4 * t ** 2 + t) * list[(i + 1)%size][1] + (t ** 3 - t ** 2) * list[(i + 2)%size][1]) / 2
            clear_canvas()
            background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            character.clip_draw((int)(frame) * 100, des, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.01)
            get_events()

size = 10
points = [(random.randint(50,1230),random.randint(50,974)) for i in range(size)]

running = True
while running:
    move_by_curve(points)
    handle_events()

close_canvas()