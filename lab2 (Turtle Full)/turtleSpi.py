import turtle

n = int(input())

if n < 2:
    print('Плохое число. Нужно 2 и более, а то уж слишком инвалид паук.')
else:

    ang = float(360/n)

    turtle.shape('turtle')

    for i in range(n):
        turtle.forward(50)
        turtle.stamp()
        turtle.backward(50)
        turtle.left(ang)


