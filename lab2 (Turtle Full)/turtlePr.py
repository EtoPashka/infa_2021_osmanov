import turtle
import math

def dug(r):
    turtle.speed(10)
    turtle.pendown()
    a = 2 * r * math.sin(math.pi/180)
    for i in range(90):
        turtle.fd(a)
        turtle.rt(2)

turtle.lt(90)
for i in range(5):
    dug(50)
    dug(10)