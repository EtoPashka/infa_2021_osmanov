import math
from random import choice, randint
from random import randint as rnd
import pygame
from pygame.draw import *

FPS = 60

TRANSPARENT = (0, 0, 0, 0)

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600



class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450, g=0.6):
        ''' 
        Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        '''
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.width = WIDTH
        self.height = HEIGHT
        self.g = g


    def move(self):
        '''
        Перемещает шар по прошествии единицы времени
        '''

        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.g
        if(self.y > self.height-self.r):
            self.y = self.height-self.r
            self.vy *= -0.7

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            width=1
        )


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f_power = 10
        self.f_on = 0
        self.an = 1
        self.color = GREY

        self.x = 40
        self.y = 450

    def fire_start(self):
        self.f_on = 1

    def fire_end(self, event):
        '''
        Выстрел шаром
        Происходит при отпускании кнопки мыши
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши
        '''
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2(
            (event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f_power * math.cos(self.an)/2
        new_ball.vy = - self.f_power * math.sin(self.an)/2
        self.f_on = 0
        self.f_power = 10
        return new_ball

    def targetting(self, event):
        '''Прицеливание. Зависит от положения мыши.'''
        if event:
            if(event.pos[0]-20):
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        width = 10
        coords = [
            (self.x, self.y),
            (self.x+(self.f_power+20)*math.cos(self.an),
             self.y+(self.f_power+20)*math.sin(self.an)),
            (self.x+(self.f_power+20)*math.cos(self.an)+width*math.sin(self.an),
             self.y+(self.f_power+20)*math.sin(self.an)-width*math.cos(self.an)),
            (self.x+width*math.sin(self.an), self.y-width*math.cos(self.an))
        ]

        polygon(self.screen, self.color, (coords), width=0)

    def power_up(self):
        if self.f_on:
            if self.f_power < 100:
                self.f_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        '''Инициализация новой цели'''
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(15, 50)
        self.vx=rnd(-7, 7)
        self.vy=rnd(-7, 7)
        self.color = GAME_COLORS[rnd(0,5)]
        self.screen = screen

    def move(self):
        '''Перемещение на текущее значение скорости'''
        self.x += self.vx
        self.y += self.vy

    def hit(self):    
        return 0

    def draw(self):
        '''Рисует крестик'''
        X, Y, R, K = self.x, self.y, self.r, 0.9
        pygame.draw.polygon(
            self.screen,
            RED,
            [(X-R, Y-R), (X-R, Y-K*R), (X+K*R, Y+R), (X+R, Y+R), (X+R, Y+K*R), (X-K*R, Y-R)]
        )
        pygame.draw.polygon(
            self.screen,
            RED,
            [(X-R, Y+R), (X-R, Y+K*R), (X+K*R, Y-R), (X+R, Y-R), (X+R, Y-K*R), (X-K*R, Y+R)]
        )

    def on_hit(self, ball: Ball):
        '''Сам по себе класс Target неуязвим'''
        return False

    def collision(self, width, height):
        '''
        Проверка столкновений с границами
        width, height - размер окна игры
        '''
        if(self.x + self.r > width):
            self.vx *= -1
            self.x = width-self.r
        elif(self.x - self.r < 0):
            self.vx *= -1
            self.x = self.r
        elif(self.y - self.r < 0):
            self.vy *= -1
            self.y = self.r
        elif(self.y + self.r > height):
            self.vy *= -1
            self.y = height-self.r

class Circle(Target):
    '''Класс целей-кругов'''
    def hit(self):
        '''При попадании шарика по цели-кругу даёт SCORE'''
        SCORE = 1
        return SCORE

    def draw(self):
        '''Рисует круг'''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            width=1
        )

    def on_hit(self, ball: Ball):
        '''Проверка на попадание шариком'''
        if ((self.x - ball.x)**2 + (self.y - ball.y)**2 < (self.r + ball.r)**2):
            return True
        else:
            return False

class Rect(Target):
    '''Класс целей-квадратов'''
    def hit(self):
        '''При попадании шарик по цели-квадрату даёт SCORE'''
        SCORE = 2
        return SCORE

    def draw(self):
        '''Рисует квадрат'''
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x-self.r, self.y-self.r, self.r*2,self.r*2)
        )
        pygame.draw.rect(
            self.screen,
            BLACK,
            (self.x-self.r, self.y-self.r, self.r*2,self.r*2),
            width=1
        )

    def on_hit(self, ball: Ball):
        '''Проверка на попадание шариком'''
        distance = self.r + math.sin(math.pi/4) * ball.r
        if (self.x - distance < ball.x < self.x + distance and self.y - distance < ball.y < self.y + distance):
            return True
        else:
            return False

class Game:
    '''Класс самой игры. 2 цели: круг и квадрат.'''
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.gun = Gun(self.screen)
        self.font = pygame.font.Font(None, 36)
        self.bullet = 0   # сколько выстрелов было произведено
        self.bulletshow = 0   # запоминает значение self.bullet при попадании для вывода на экран
        self.balls = []       # шары, выстреливаемые пушкой
        self.points = 0
        self.targets = [Circle(self.screen), Rect(self.screen)]
        self.show_result = 0   # значение, которое используется как "таймер" показа результата при попадании в цель
        self.pause = False
        self.finished = False


    def draw(self, background):
        '''Отрисовка игры'''
        self.screen.fill(background)
        for target in self.targets:
            target.draw()
        self.gun.draw()
        for ball in self.balls:
            ball.draw()
        self.drawscore()
        self.pause = False
        if self.show_result:
            self.showtext()
            self.show_result -= 1
            self.pause = True
        pygame.display.update()
        self.clock.tick(FPS)

    def catch_event(self):
        '''Отклик на действия игрока'''        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if(not self.pause):
                    self.gun.fire_start()
            elif event.type == pygame.MOUSEBUTTONUP:
                if(not self.pause):
                    self.balls.append(self.gun.fire_end(event))
                    self.bullet += 1
            elif event.type == pygame.MOUSEMOTION:
                self.gun.targetting(event)

    def proceed(self):
        '''Передвижение объектов'''
        for ball in self.balls:
            ball.move()
            for target in self.targets:
                if self.hittest(ball):
                    self.bulletshow = self.bullet
                    self.bullet = 0
                    self.balls = []
                    self.show_result = 100
        self.gun.power_up()
        for target in self.targets:
            target.move()
            target.collision(self.width, self.height)
    
    def get_status(self):
        return self.finished

    def hittest(self, ball: Ball):
        '''Проверка на попадание в цель'''
        for target in self.targets:
            if target.on_hit(ball):
                self.points += target.hit()
                if type(self.targets.pop(self.targets.index(target))) == Circle:
                    self.targets.append(Circle(self.screen))
                else:
                    self.targets.append(Rect(self.screen))                
                return True
        return False

    def drawscore(self):
        '''Вывод очков на экран'''
        text = self.font.render('Очки: ' + str(self.points), True, BLACK)
        self.screen.blit(text, (10, 10))

    def showtext(self):
        '''Выводит, сколько выстрелов потрачено на поражение цели'''
        if (11 <= self.bulletshow % 100 <= 14):
            word = ' выстрелов'
        elif (2 <= self.bulletshow % 10 <= 4):
            word = ' выстрела'
        elif self.bulletshow % 10 == 1:
            word = ' выстрел'
        else: 
            word = ' выстрелов'
        text = self.font.render('Вы уничтожили цель за ' + str(self.bulletshow) + word, True, BLACK)
        self.screen.blit(text, (180, 250))

    def finish(self):
        pygame.quit()




game = Game(WIDTH, HEIGHT)

while not game.get_status():
    game.draw(WHITE)
    game.catch_event()
    game.proceed()

game.finish()

