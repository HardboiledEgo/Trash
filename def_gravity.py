from math import sqrt
def gravity(object_y, ground_level, g, t):
    speed = int(sqrt(2*g*t))
    if object_y+speed > ground_level:
        object_y = ground_level
        jump_try = 0
    if object_y < ground_level:
        object_y += speed

    return(object_y)