import pickle

# layer 0: Background Objects
# layer 1: John
# layer 2: Block Objects
# layer 3: Enemy Objects
# layer 4: Cannon left Objects
# layer 5: Cannon right Objects
# layer 6: Bullet Objects
# layer 7: Trap Objects
# layer 8: Goal Objects
objects = [[], [], [], [], [], [], [], [], [], []]


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for l in objects:
        l.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o


def save():
    with open('game.sav', 'wb') as f:
        pickle.dump(objects, f)
    pass

def load():
    global objects
    with open('game.sav', 'rb') as f:
        objects = pickle.load(f)
    pass