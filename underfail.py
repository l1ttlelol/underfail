import pygame
import random
pygame.init()

Black = (0,0,0) 
White = (255,255,255)
boudary_x = (400)
boundary_y = (400)
boundary_length = (1120)
boundary_height = (580)

size = (1920,1080)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("underfail")
done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			screen.fill(Black)
			done = True

	screen.fill(Black)
	pygame.draw.rect(screen,White,[400,400,1120,580],2)

	clock.tick(60)
pygame.quit()
