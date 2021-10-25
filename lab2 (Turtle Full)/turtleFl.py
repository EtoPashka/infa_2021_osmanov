import turtle
import math

def rnd(r, direction):
    turtle.pendown()
    if direction == 'l':
        a = 2 * r * math.sin(math.pi/180)
        for i in range(180):
            turtle.fd(a)
            turtle.lt(2)
    elif direction == 'r':        
        a = 2 * r * math.sin(math.pi/180)
        for i in range(180):
            turtle.fd(a)
            turtle.rt(2)

for i in range(3):
    rnd(30, 'l')
    rnd(30, 'r')
    turtle.lt(120)