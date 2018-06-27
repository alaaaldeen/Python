import random

def random_walk(n):
    """Return the coordinats after 'n' blocks"""
    x = 0
    y = 0
    direct = ['N','S','E','W']


    for i in range(n):
        d = random.choice(direct)

        if d == 'N':
            x += 1

        elif d == 'S':
            x -= 1

        elif d == 'E':
            y += 1

        else:
            y -= 1
    return (x, y)

for i in range(25):
    walk = random_walk(10)
    print walk, "Distance from home = ", abs(walk[0]) + abs(walk[1])
