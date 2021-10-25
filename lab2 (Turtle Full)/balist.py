import turtle
import math

t = turtle.Turtle()

t.speed(9)
t.pu()
t.fd(1000)
t.pd()
t.bk(1400)

t.shape('circle')

ang = 60
v = 40

Vx = v * math.cos(ang * math.pi / 180)
Vy = v * math.sin(ang * math.pi / 180)

g = -10

dt = 0.1

for i in range(1000):
    t.goto(t.xcor() + Vx*dt, t.ycor() + Vy*dt + g*dt**2/2)
    if Vx < 5:
        break
    Vy += g*dt
    if t.ycor() <= 0:
        Vy = -Vy * 3 / 4
        t.goto(t.xcor(), 0)
        if Vy < 5:
            for k in range (1000):
                t.goto(t.xcor() + Vx*dt, 0)
                Vx = Vx * 24/25
                if Vx < 5:
                    break
    
        
turtle.exitonclick()