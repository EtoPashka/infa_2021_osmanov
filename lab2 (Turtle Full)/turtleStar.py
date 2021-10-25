import turtle as tt

def stars180(n):
    for i in range(n):
        tt.lt(180-(180 / n))
        tt.fd(100)

n = int(input())



tt.shape('turtle')

stars180(n)

tt.exitonclick()



