import turtle
import math

def mnog(n, r):
    turtle.penup()
    turtle.fd(r)
    turtle.lt(90+180/n)
    turtle.pendown()
    a = 2 * r * math.sin(math.pi/n)
    for i in range(n):
        turtle.fd(a)
        turtle.lt(360/n)
    turtle.penup()
    turtle.rt(90+180/n)
    turtle.bk(r)
    turtle.pendown()

for i in range(10):
    mnog(3+i, 20 + i * 10)
