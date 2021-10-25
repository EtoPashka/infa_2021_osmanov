import pygame
from pygame.draw import *
from random import randint, choice

import json, operator

print('Введите ваше имя:', end=' ')

PLAYER_NAME = input()

pygame.init()
pygame.font.init()
start_text = pygame.font.SysFont('Comic Sans MS', 30)


FPS = 30                  
BORDERS = (1200, 1000)      #границы области игры
DIFFICULTY = 1              #сложность игры (множитель скорости передвижения)
NUMBER_OF_BALLS = 5         #общее количество шариков
FAIL_SCORE = 50             #сколько очков отнимется за промах
GAME_TIME = 10              #время на игру в секундах

#ШАРИКИ - мин. и макс. радиусы и скорости
MIN_R = 40
MAX_R = 70
MIN_V = 3
MAX_V = 12
BALL = 'Шар'
BALL_SCORE = 300

#ПРЯМОУГОЛЬНИКИ - мин. и макс. длины сторон и скорости
MIN_B = 80
MAX_B = 150
MIN_SP_V = 15
MAX_SP_V = 25
RECT = 'Прямоугольник'
RECT_SCORE = 500


screen = pygame.display.set_mode(BORDERS)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
#класс шарика
    def __init__ (self, coord, velocity, color, r):
        '''задаём координаты, скорость, цвет и радиус шарика'''
        self.coord = coord
        self.velocity = velocity
        self.color = color
        self.r = r
        self.name = BALL
        self.points = BALL_SCORE

    def move(self, dt):
        '''задаём смещение координаты шарика'''
        self.coord[0] += self.velocity[0]*dt
        self.coord[1] += self.velocity[1]*dt

    def collision(self, borders):
        '''проверяем шарик на столкновение с границей'''
        if self.coord[0] <= self.r or self.coord[0] >= borders[0] - self.r:
            self.velocity[0] = - self.velocity[0]

        if self.coord[1] <= self.r or self.coord[1] >= borders[1] - self.r:
            self.velocity[1] = - self.velocity[1]
            
    def event(self, event):
        '''проверяем, прошло ли событие (клик мыши) в области шарика'''
        if (event.pos[0] - self.coord[0])**2 + (event.pos[1] - self.coord[1])**2 <= self.r**2:
            return True
        else:
            return False

    def position_update(self, difficulty, borders):
        '''обновляет положение шариков'''
        self.move(difficulty)
        self.collision(borders)
        circle(screen, self.color, self.coord, self.r)

class Special:
#класс особого объекта (прямоугольник)
    def __init__ (self, coord, velocity, color, bord):
        '''задаём координаты, скорость, цвет и размер объекта'''
        self.coord = coord
        self.velocity = velocity
        self.color = color
        self.bord = bord
        self.name = RECT
        self.points = RECT_SCORE

    def move(self, dt):
        '''задаём смещение координаты объекта'''
        self.coord[0] += self.velocity[0]*dt
        self.coord[1] += self.velocity[1]*dt

    def v_change(self):
        '''задаём новую скорость'''
        self.velocity[0] = randint(MIN_SP_V, MAX_SP_V)*choice(range(-1, 2, 2))
        self.velocity[1] = randint(MIN_SP_V, MAX_SP_V)*choice(range(-1, 2, 2))
    def c_change(self):#не используется в целях сохранения жизни эпилептикам
        '''задаём новый цвет'''
        self.color = COLORS[randint(0, len(COLORS)-1)]

    def collision(self, borders):
        '''проверяем объект на столкновение с границей'''
        if self.coord[0] <= 0 or self.coord[0] >= borders[0] - self.bord[0]:
            self.velocity[0] = - self.velocity[0]
            if self.coord[0] <= 0:
                self.coord[0] = 0
            else:
                self.coord[0] = borders[0] - self.bord[0]

        if self.coord[1] <= 0 or self.coord[1] >= borders[1] - self.bord[1]:
            self.velocity[1] = - self.velocity[1]
            if self.coord[1] <= 0:
                self.coord[1] = 0
            else:
                self.coord[1] = borders[1] - self.bord[1]
    
    def event(self, event):
        '''проверяем, прошло ли событие (клик мыши) в области прямоугольника'''
        if self.coord[0] <= event.pos[0] <= self.coord[0]+self.bord[0] and self.coord[1] <= event.pos[1] <= self.coord[1]+self.bord[1]:
            return True
        else:
            return False

    def position_update(self, difficulty, borders):
        '''обновляет положение прямоугольников'''
        self.v_change()
        #self.c_change()
        self.move(difficulty)
        self.collision(borders)
        rect(screen, self.color, (self.coord[0], self.coord[1], self.bord[0], self.bord[1]))  
    
# КЛАСС НАШЕЙ ИГРЫ
class Game:
    def __init__(self, difficulty, borders, names_of_obj, appear_chances, player_name):
        '''создаём объект из класса игра, у которого задаются сложность, границы игры, названия используемых объектов и шансы появления каждого типа объекта'''        
        self.difficulty = difficulty
        self.borders = borders
        self.names = names_of_obj
        self.rates = appear_chances
        '''также создаётся отдельно список всех объектов игры, которые видит игрок, но изначально он пуст и требует дополнительной инициализации'''
        self.pool = []                    

        self.score = 0                    #тут будут засчитываться очки
        self.fail = FAIL_SCORE            #столько будет отниматься за промах
        self.log = ['Last game log for ' + player_name + ':\n']                     #это лог для последней игры

        self.score_text = pygame.font.SysFont('Comic Sans MS', 30)           #параметры текста для подсчёта очков
        

    def default_object_create(self, name_of_obj):
        '''создаёт объект игры'''
        if name_of_obj == BALL:
            coordinates = [randint(MAX_R, BORDERS[0] - MAX_R), randint(MAX_R, BORDERS[1] - MAX_R)]
            velocity = [randint(MIN_V, MAX_V)*choice(range(-1, 2, 2)), randint(MIN_V, MAX_V)*choice(range(-1, 2, 2))]
            color = COLORS[randint(0, len(COLORS)-1)]
            r = randint(MIN_R, MAX_R)
            return Ball(coordinates, velocity, color, r)

        elif name_of_obj == RECT:
            coordinates = [randint(0, BORDERS[0] - MAX_B), randint(0, BORDERS[1] - MAX_B)]
            velocity = [randint(MIN_SP_V, MAX_SP_V)*choice(range(-1, 2, 2)), randint(MIN_SP_V, MAX_SP_V)*choice(range(-1, 2, 2))]
            color = COLORS[randint(0, len(COLORS)-1)]
            bord = (randint(MIN_B, MAX_B), randint(MIN_B, MAX_B))
            return Special(coordinates, velocity, color, bord)

    def init_pool(self, num_of_obj):
        '''инициализация списка объектов'''
        for i in range(num_of_obj):
            self.pool.append(self.default_object_create(self.names[0]))

    def update_position(self):
        '''обновляет координаты объектов, используя функции соответствующего объекту класса'''
        for object in self.pool:
            object.position_update(self.difficulty, self.borders)

    def update_score(self):
        '''обновляет счётчик очков'''
        textsurface = self.score_text.render('Score: ' + str(self.score), False, WHITE)
        screen.blit(textsurface,(0, 0))

    def timer_update(self, time_left):
        '''показывает время до конца игры'''
        textsurface = self.score_text.render('Time left: ' + str(time_left) + 's', False, WHITE)
        screen.blit(textsurface,(0, BORDERS[1] -  50))

    def click_respond(self, event):
        '''реакция на клик мыши'''
        no_click = True
        for object in self.pool:
            if object.event(event):
                no_click = False
                self.score += object.points
                self.log.append('+' + str(object.points) + '!\n')
                self.pool.pop(self.pool.index(object))
                for i in range(len(self.names)):
                    if randint(1, sum(self.rates[i:])) <= self.rates[i]:
                        self.pool.append(self.default_object_create(self.names[i]))
                        break
                break
           
        if self.score >= self.fail and no_click:
            self.score -= self.fail
            self.log.append('-' + str(self.fail) + '!\n')
                        



NAMES = [BALL, RECT]
CHANCES = [5, 2]

game = Game(DIFFICULTY, BORDERS, NAMES, CHANCES, PLAYER_NAME)
game.init_pool(NUMBER_OF_BALLS)

textsurface = start_text.render('Press LMB to start', False, WHITE)
screen.blit(textsurface,(0,0))
pygame.display.update()



finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            finished = True
        if event.type == pygame.QUIT:
            pygame.quit()



pygame.display.update()
clock = pygame.time.Clock()


finished = False
start_time = pygame.time.get_ticks()              #запуск таймера

while not finished:

    clock.tick(FPS)
    game.update_position()
    game.update_score()
    game.timer_update(GAME_TIME - int((pygame.time.get_ticks() - start_time)/1000))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.click_respond(event)
    
    
    screen.fill(BLACK)
    if pygame.time.get_ticks() - start_time >= GAME_TIME * 1000:          #проверка таймера
        finished = True

pygame.quit()
pygame.font.quit()

game.log.append('Final score: ' + str(game.score) + '!')


#Простенький лог
with open("last_game_log.txt", 'w') as f:    
    for str in game.log:
        f.write(str)

#Чтение таблицы, добавление последнего результата, сортировка и запись
with open("best.json", 'r') as f:
    loaded = json.load(f)

loaded['results'].append({'name': PLAYER_NAME, 'points': game.score})
loaded['results'].sort(key = operator.itemgetter('points'), reverse = True)
loaded['games count'] += 1

with open("best.json", 'w') as f:
    json.dump(loaded, f)

#Тут была запись в best.txt
'''
position = 0
table = []

with open('best.txt') as file:
    table = file.readlines()

with open('best.txt', 'w') as output:
    for player in table:
        if game.score > int(player.rstrip().split(': ')[-1]):            
            position = table.index(player) + 1
            table.insert(table.index(player), PLAYER_NAME + ': ' + str(game.score) + '\n')
            break
    if position == 0:
        table.append(PLAYER_NAME + ': ' + str(game.score) + '\n')
    if len(table) > 5:
        table.pop()
    for place in table:
        output.write(place)
'''