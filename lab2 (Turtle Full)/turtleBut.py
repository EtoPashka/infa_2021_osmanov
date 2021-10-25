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
        

turtle.lt(90)
for i in range(5):
    rnd(50 + 20*i, 'l')
    rnd(50 + 20*i, 'r')
        

