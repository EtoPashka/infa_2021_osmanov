import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

bgcolor = (217, 217, 217)

rect(screen, bgcolor, (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)

circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 20, 1)
circle(screen, (0, 0, 0), (150, 180), 8)

circle(screen, (255, 0, 0), (250, 180), 15)
circle(screen, (0, 0, 0), (250, 180), 15, 1)
circle(screen, (0, 0, 0), (250, 180), 7)

rect(screen, (0, 0, 0), (150, 250, 100, 20))



polygon(screen, (0, 0, 0), [(104, 118), (183, 167), (178, 175), (100, 125)])


polygon(screen, (0, 0, 0), [(299, 137), (220, 166), (223, 175), (302, 145)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False 

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()