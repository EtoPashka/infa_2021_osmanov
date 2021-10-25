import turtle

pochta = []

font = open('font.txt')

for line in font:   
    pochta.append(line.rstrip().split(', '))

font.close()

#i0 = ('pdn', 'up', 'up', 'rt', 'dn', 'dn', 'lt', 'pup', 'rt', 'mv')
#i1 = ('pup', 'up', 'pdn', 'dup','dn', 'dn', 'pup', 'mv')
#i2 = ('pup', 'up', 'up', 'pdn', 'rt', 'dn', 'ddn', 'rt', 'pup', 'mv')
#i3 = ('pdn', 'dup', 'lt', 'dup', 'lt', 'pup', 'dn', 'dn', 'rt', 'mv')
#i4 = ('pup', 'up', 'up', 'pdn', 'dn', 'rt', 'pup', 'up', 'pdn', 'dn', 'dn', 'pup', 'mv')
#i5 = ('pdn', 'rt', 'up', 'lt', 'up', 'rt', 'pup', 'dn', 'dn', 'mv')
#i6 = ('pup', 'up', 'pdn', 'rt', 'dn', 'lt', 'up', 'dup', 'pup', 'dn', 'dn', 'mv')
#i7 = ('pdn', 'up', 'dup', 'lt', 'pup', 'dn', 'dn', 'rt', 'mv')
#i8 = ('pdn', 'up', 'up', 'rt', 'dn', 'dn', 'lt', 'pup', 'up', 'pdn', 'rt', 'pup', 'dn', 'mv')
#i9 = ('pdn', 'dup', 'up', 'lt', 'dn', 'rt', 'pup', 'dn', 'mv')

#for i in i0, i1, i2, i3, i4, i5, i6, i7, i8, i9:
#    pochta.append(i) 

print('Введите натуральное число:', end = ' ')

i = input()

t = turtle.Turtle()
t.color('blue')
t.speed(9)
t.width(4)
t.penup()
t.bk(400)
t.speed(2)

for e in i:
    for act in pochta[int(e)]:
        if act == 'pup':
            t.penup()
        elif act == 'pdn':
            t.pendown()
        elif act == 'mv':
            t.goto(t.xcor()+20, t.ycor())
        elif act == 'up':
            t.goto(t.xcor(), t.ycor()+40)
        elif act == 'dn':
            t.goto(t.xcor(), t.ycor()-40)
        elif act == 'rt':
            t.goto(t.xcor()+40, t.ycor())
        elif act == 'lt':
            t.goto(t.xcor()-40, t.ycor())
        elif act == 'dup':
            t.goto(t.xcor()+40, t.ycor()+40)
        elif act == 'ddn':
            t.goto(t.xcor()-40, t.ycor()-40)

turtle.exitonclick()
