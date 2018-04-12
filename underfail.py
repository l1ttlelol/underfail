import pygame
import random
pygame.init()

Black = (0,0,0) 
White = (255,255,255)

size = (1920,1080)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("template")
done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			screen.fill(Black)
			done = True

	screen.fill(Black)

	clock.tick(60)
pygame.quit()
