import pygame
from pygame.locals import*
img = pygame.image.load('soul sprite.png')
img = pygame.transform.scale(img,(70,70))
pygame.init()

# The value for colors
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)

PI = 3.141592653

#creating the window
size = (700,500)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("practice")
quit = False
clock = pygame.time.Clock()

#quitting the window part 1
while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			screen.fill(Black)
			quit = True

	#Drawing on the window
	screen.fill(White)
	screen.blit(img,(0,0))
	pygame.display.flip()		                 
	
	#quitting the window part 2
	clock.tick(60)
pygame.quit()
