import turtle

turtle.shape('turtle')

for i in range(10):
    turtle.penup()
    turtle.goto((i)*(-5), (i)*(-5))
    turtle.pendown()
    for k in range(4):
        turtle.forward(10+i*10)
        turtle.left(90)
    
