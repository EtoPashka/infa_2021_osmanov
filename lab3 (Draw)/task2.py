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

def clouds(x, y, width, height, brightness):
    '''
    предполагается, что яркость от 0 до 100 (иначе ярче фона)
    '''
    if brightness > 100:
        brightness = 100
    ellipse(screen, (brightness, brightness, brightness), (x, y, width, height))


def ghost(x, y, r, height):
    '''первичный вариант призрака'''
    circle(screen, (179, 179, 179), (x, y), r)
    polygon(screen, (179, 179, 179), ([x+r,y], [x+r*1.2,y+height], [x-r*1.2, y+height], [x-r, y]))
    for i in range (6):
	    R = int(r//(2.5))
	    circle(screen, (179, 179, 179), ((x-r)+ R*i, y+height), R)
    for i in range (6):
	    R = int(r//(2.5))
	    circle(screen, (0, 0, 0), ((x-r)+ R*i, y+height+R), R)  
	# глаза
    ellipse(screen,(0, 191, 255), (x-0.5*r, y-0.5*r, r*0.25, r*0.5))
    ellipse(screen,(0, 191, 255), (x+0.25*r, y-0.5*r, r*0.25, r*0.5))
    ellipse (screen, (0, 0, 0), (x-0.50*r, y-0.3*r, r*0.25, r*0.25))
    ellipse (screen, (0, 0, 0), (x+0.25*r, y-0.3*r, r*0.25, r*0.25))

def ghost_smart(x, y, r, image):
    '''Используется картинка'''
    new_image = pygame.transform.scale(image, (r*6, r*5))
    screen.blit(new_image, (x-2.5*r, y-0.3*r))
    circle(screen, (179, 179, 179), (x, y), r)
	
	# глаза
    ellipse(screen,(0, 191, 255), (x-0.5*r, y-0.5*r, r*0.25, r*0.5))
    ellipse(screen,(0, 191, 255), (x+0.25*r, y-0.5*r, r*0.25, r*0.5))
    ellipse (screen, (0, 0, 0), (x-0.50*r, y-0.3*r, r*0.25, r*0.25))
    ellipse (screen, (0, 0, 0), (x+0.25*r, y-0.3*r, r*0.25, r*0.25))




pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))
ghost_image = pygame.image.load('ghost.png').convert_alpha()


# фон
rect(screen, (105, 105, 105), [0, 0, 400, 150])

# луна
circle (screen, (255, 255, 255), (350, 50), 20)

clouds(250, 120, 140, 40, 40)
clouds(100, 20, 140, 40, 70)

house(30,100,200,200)

clouds(200, 50, 140, 40, 10)


ghost_smart(300, 250, 20, ghost_image)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()