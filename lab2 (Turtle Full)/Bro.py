import turtle as tt
import random as rd

tt.shape('turtle')
tt.speed(9)

for i in range(100):
    tt.lt(360*rd.random())
    tt.fd(50*rd.random())

tt.exitonclick()