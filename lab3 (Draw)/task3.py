import pygame
from pygame.draw import *



def house(x, y, width, height): 
	'''
	x, y - координаты левого верхнего угла дома
	width - ширина дома
	height - высота дома
	'''
	# основа дома
	polygon(screen, (40, 34, 11), ([x,y+height], [x+width, y+height], [x+width, y], [x, y]))

	# окна снизу
	polygon(screen, (43, 17, 0), ([x+(width//8),y+4*(height//6)], [x+2*(width//8), y+4*(height//6)], 
                                  [x+2*(width//8), y+5*(height//6)], [x+(width//8), y+5*(height//6)]))
	polygon(screen, (43, 17, 0), ([x+3*(width//8),y+4*(height//6)], [x+4*(width//8), y+4*(height//6)], 
                                  [x+4*(width//8), y+5*(height//6)], [x+3*(width//8), y+5*(height//6)]))
	polygon(screen, (212, 170, 0), ([x+5*(width//8),y+4*(height//6)], [x+6*(width//8), y+4*(height//6)], 
                                    [x+6*(width//8), y+5*(height//6)], [x+5*(width//8), y+5*(height//6)]))
	# окна сверху
	polygon(screen, (72, 62, 55), ([x+(width//5),y], [x+2*(width//5), y], 
                                      [x+2*(width//5), y + (height//2)], [x+(width//5), y + (height//2)]))
	polygon(screen, (72, 62, 55), ([x+3*(width//5),y], [x+4*(width//5), y], 
                                      [x+4*(width//5),  y + (height//2)], [x+3*(width//5),  y + (height//2)]))
	
	# трубы
	polygon(screen, (26, 26, 26), ([x+(width//6),y], [x+2*(width//6), y], 
                                   [x+2*(width//6), y - height//4], [x+(width//6), y - height//4]))
	polygon(screen, (26, 26, 26), ([x+3*(width//6),y], [x+4*(width//6), y], 
                                   [x+4*(width//6), y - height//6], [x+3*(width//6), y - height//6]))
	# крыша
	polygon(screen, (0, 0, 0), ([x-(width//8),y], [x+width+(width//8), y], 
                                 [x+width, y -(height//8)], [x, y - (height//8)]))
	# балкон (нижняя часть)
	polygon(screen, (26, 26, 26), ([x-(width//8),y + (height//2)], [x+width+(width//8), y + (height//2)], 
                                  [x+width+(width//8), y + (height//2)+(height//10)], [x-(width//8),y + (height//2)+(height//10)]))
	# перегородка балкона (края)
	polygon(screen, (26, 26, 26), ([x-(width//8),y + (height//2)], [x+(width//25), y + (height//2)], 
                                  [x+(width//25), y + (height//2)-(height//10)], [x-(width//8), y + (height//2)-(height//10)]))
	polygon(screen, (26, 26, 26), ([x+width+(width//8) - (height//10),y + (height//2)], [x+width+(width//8), y + (height//2)], 
                                  [x+width+(width//8), y + (height//2)-(height//10)], [x+width+(width//8) - (height//10), y + (height//2)-(height//10)]))
    # вставки в перегородке
	i=1
	while i < 11:
		polygon(screen, (26, 26, 26), ([x+i*(width//10), y + (height//2)], [x+(i+1)*(width//10), y + (height//2)], 
                                      [x+(i+1)*(width//10),  y + (height//2)-(height//10)], [x+i*(width//10),  y + (height//2)-(height//10)]))
		i+=2
    # верхняя часть
	polygon(screen, (26, 26, 26), ([x-(width//8),y + (height//2)-(height//10)], [x+width+(width//8), y + (height//2)-(height//10)], [x+width+(width//8), y + (height//2)-(height//9)], [x-(width//8), y + (height//2)-(height//9)]))

def clouds(x, y, width, height, brightness, transparent=False):
    '''
    Предполагается, что яркость (brightness) от 0 до 100 (иначе ярче фона)
    transparent - будет ли прозрачной
    '''
    if (transparent):
        cloud_screen = pygame.Surface((794, 1123))
        cloud_screen.set_alpha(200)
        cloud_screen.fill((105, 105, 105))
        cloud_screen.set_colorkey((105, 105, 105))
        scr = cloud_screen
    else:
        scr = screen

    if brightness > 100:
        brightness = 100
    ellipse(scr, (brightness, brightness, brightness), (x, y, width, height))
    if (transparent):
        screen.blit(scr, (0, 0))


def ghost_smart(x, y, r, image, transparent=False, reverse=False):
    '''
    Используется картинка
    transparent - будет ли прозрачной
    reverse - будет ли отзеркаленной
    '''    
    if (transparent):        
        ghost_screen = pygame.Surface((794, 1123))
        ghost_screen.set_alpha(180)
        ghost_screen.fill((0, 0, 0))
        ghost_screen.set_colorkey((0, 0, 0))
        scr = ghost_screen
    else:
        scr = screen
    new_image = pygame.transform.scale(image, (r*6, r*5))

    sign = 1
    if (reverse):
        sign = -1
        reverse_image = pygame.transform.flip(new_image, True, False)
        scr.blit(reverse_image, (x-3.4*r, y-0.3*r))
    else:
        scr.blit(new_image, (x-2.5*r, y-0.3*r))

    circle(scr, (179, 179, 179), (x, y), r)
	
	# глаза
    circle(scr, (135, 205, 222), (x-0.5*sign*r, y-0.1*r), 2*r//7)
    circle(scr, (135, 205, 222), (x+0.3*sign*r, y-0.3*r), 2*r//7)
    x_eye = x-0.57*sign*r
    y_eye = y-0.1*r
    r_eye = r//8
    circle(scr, (0, 0, 0), (x_eye, y_eye), r_eye)
    circle(scr, (255, 255, 255), (x_eye+0.7*sign*r_eye, y_eye-0.7*r_eye), r_eye//2)
    x_eye = x+0.23*sign*r
    y_eye = y-0.3*r
    circle(scr, (0, 0, 0), (x_eye, y_eye), r_eye)
    circle(scr, (255, 255, 255), (x_eye+0.7*sign*r_eye, y_eye-0.7*r_eye), r_eye//2)

    if (transparent):
        screen.blit(scr, (0, 0))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
screen.fill((0, 0, 0))
ghost_image = pygame.image.load('ghost.png').convert_alpha()






# фон
rect(screen, (105, 105, 105), [0, 0, 794, 468])

# луна
circle(screen, (255, 255, 255), (715, 100), 70)

house(272, 415, 209, 291)
house(579, 267, 209, 291)

clouds(40, 106, 620, 80, 51)
clouds(347, 70, 460, 75, 77)
clouds(470, 165, 700, 80, 77)

clouds(359, 242, 540, 75, 20, True)
clouds(139, 433, 760, 77, 77, True)
clouds(344, 518, 570, 80, 77, True)
clouds(0, 634, 440, 70, 77, True)

house(20, 529, 209, 291)

ghost_smart(629, 828, 35, ghost_image)
ghost_smart(714, 662, 20, ghost_image, True)
ghost_smart(738, 720, 20, ghost_image, True)
ghost_smart(537, 850, 20, ghost_image, True)
ghost_smart(134, 884, 20, ghost_image, True, True)
ghost_smart(162, 941, 20, ghost_image, True, True)
#ghost_smart(400, 500, 80, ghost_image, True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()