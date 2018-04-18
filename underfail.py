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
y_acceleration = 0
x_acceleration = 0
			
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			screen.fill(Black)
			done = True


	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT and x_acceleration < 10:
			x_acceleration += 1
		if event.key == pygame.K_LEFT and x_acceleration > -10:
			x_acceleration -= 1
		if event.key == pygame.K_UP and y_acceleration > -10:
			y_acceleration -= 1
		if event.key == pygame.K_DOWN and y_acceleration < 10:
			y_acceleration += 1
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			x_acceleration = 0
		if event.key == pygame.K_LEFT:
			x_acceleration = 0
		if event.key == pygame.K_UP:
			y_acceleration = 0
		if event.key == pygame.K_DOWN:
			y_acceleration = 0
	if player_y > 400 and player_y < 980:
		player_y += y_acceleration

	if player_x > 400 and player_x < 1520:
		player_x += x_acceleration

	screen.fill(Black)
	pygame.draw.rect(screen,White,[400,400,1120,580],2)
	pygame.draw.rect(screen,White,[player_x,player_y,70,70])

	if player_health < 1:
		screen.fill(Black)
	pygame.display.flip()		                 

	clock.tick(60)
pygame.quit()