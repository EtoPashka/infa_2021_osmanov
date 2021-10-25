from random import randint
import turtle

s = 200
wd = 15
pl = s - wd

sq = turtle.Turtle()
sq.pu()
sq.goto(s, s)
sq.width(3)
sq.speed(9)
sq.pd()
for coord in (s, -s), (-s, -s), (-s, s), (s, s):
    sq.goto(coord)


number_of_turtles = 10
steps_of_time_number = 100


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]


Vx = [randint(-10, 10) for i in range(number_of_turtles)]                    #задаём составляющие скоростей черепашкам (далее я буду называть их шариками)
Vy = [randint(-10, 10) for i in range(number_of_turtles)]

for unit in pool:
    unit.shapesize(1, 1, 1)
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-pl, pl), randint(-pl, pl))

full = []

for i in range(number_of_turtles):                                          #делаем список из списков данных о шариках и их скоростях
    full.append([pool[i], Vx[i], Vy[i]])


for i in range(steps_of_time_number):                                  
    for unit in full:                                        #используем созданный список для задания движения черепашек
       
        if unit[0].xcor() <= -pl:                            # 4 if'а для проверки границы, а чтобы шарик точно за неё не вылетел, смещаем его на границу перед движением
            unit[1] = - unit[1]
            unit[0].goto(-pl, unit[0].ycor())
        if unit[0].xcor() >= pl:
            unit[1] = - unit[1]
            unit[0].goto(pl, unit[0].ycor())
        
        if unit[0].ycor() <= -pl:
            unit[2] = - unit[2]
            unit[0].goto(unit[0].xcor(), -pl)
        if unit[0].ycor() >= pl:
            unit[2] = - unit[2]
            unit[0].goto(unit[0].xcor(), pl)

        for other in full:                                    #other для  другого шарика
            y = unit[0].ycor() - other[0].ycor()
            x = unit[0].xcor() - other[0].xcor()
            dist = (x**2 + y**2)**(0.5)
            if unit[0] != other[0] and dist <= 20:           #вычисления производятся на основе того, что вдоль оси столкновения шары просто обмениваются скоростями, а перпендикулярно ей ничего не меняется
                sin = y / dist
                cos = x / dist
                dv1 = unit[1] * cos + unit[2] * sin          #составляющие при лобовом столкновении
                dv2 = other[1] * cos + other[2] * sin        #составляющие при лобовом столкновении
                dc1 = -unit[1] * sin + unit[2] * cos          # неизменные составляющие
                dc2 = -other[1] * sin + other[2] * cos        # неизменные составляющие
                unit[1] = dv2 * cos - dc1 * sin              # влияние на x и y составляющие
                unit[2] = dv2 * sin + dc1 * cos
                other[1] = dv1 * cos - dc2 * sin
                other[2] = dv1 * sin + dc2 * cos
                other[0].goto(other[0].xcor()+other[1], other[0].ycor()+other[2])    #перемещаем другой шарик тоже на всякий случай    

        unit[0].goto(unit[0].xcor()+unit[1], unit[0].ycor()+unit[2]) #итоговое перемещение шарика
