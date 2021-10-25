import turtle

turtle.shape('turtle')

ang = 0.0

while turtle.distance(0, 0) < 90:
    ang = turtle.distance(0, 0) * 40
    turtle.fd(1)
    ang = turtle.distance(0, 0) * 40 - ang
    turtle.lt(ang)
