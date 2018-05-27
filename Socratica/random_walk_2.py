import random

def random_walk_2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(1, 0), (-1, 0),( 0, 1), (0, -1)])
        x += dx
        y += dy
    return (x, y)

#for i in range(25):
#    walk = random_walk_2(10)
#    print walk, "Distance from home = ", abs(walk[0]) + abs(walk[1])
number_of_walk = 30000

for walk_length in range(1, 31):
    no_transport = 0 # Number of walks 4 or fewer blocks from home
    for i in range(number_of_walk):  #for each number of walk lenght(n) try 30K
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walk
    print "Walk size = ", walk_length, " / %  of no trasport =  ", 100*no_transport_percentage
