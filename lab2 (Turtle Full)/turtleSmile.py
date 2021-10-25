import turtle
import math

def dug(r):
    turtle.speed(10)
    turtle.pendown()
    a = 2 * r * math.sin(math.pi/180)
    turtle.rt(1)
    for i in range(90):
        turtle.fd(a)
        turtle.rt(2)
    turtle.lt(1)

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


turtle.speed(10)
turtle.penup()
turtle.forward(100)
turtle.lt(90)
turtle.pendown()
turtle.color('black', 'yellow')
turtle.begin_fill()
rnd(100, 'l')
turtle.end_fill()
turtle.color('black', 'blue')
turtle.penup()
turtle.goto(-25, 35)
turtle.pendown()
turtle.begin_fill()
rnd(14, 'l')
turtle.end_fill()
turtle.penup()
turtle.goto(25, 35)
turtle.pendown()
turtle.begin_fill()
rnd(14, 'r')
turtle.end_fill()
turtle.penup()
turtle.width(8)
turtle.lt(180)
turtle.goto(0, 10)
turtle.pendown()
turtle.fd(15)
turtle.penup()
turtle.goto(50, -20)
turtle.color('red', 'blue')
turtle.pendown()
dug(50)