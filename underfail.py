import pygame
import random
pygame.init()

Black = [0,0,0] 
White = (255,255,255)
boudary_x = (400)
boundary_y = (400)
boundary_length = (1120)
boundary_height = (580)
player_health = (100)
player_x = (700)
player_y = (700)
player = (player_x,player_y,player_health)

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


	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			player_x = player_x +1
		if event.key == pygame.K_LEFT:
			player_x = player_x -1
		if event.key == pygame.K_UP:
			player_y = player_y -1
		if event.key == pygame.K_DOWN:
			player_y = player_y +1

	screen.fill(Black)
	pygame.draw.rect(screen,White,[400,400,1120,580],2)
	pygame.draw.rect(screen,White,[player_x,player_y,70,70])


	if player_health < 1:
		screen.fill(Black)
	pygame.display.flip()		                 

	clock.tick(60)
pygame.quit()