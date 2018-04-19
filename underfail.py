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
projectile_x = random.randrange(400,1520)
projectile_y = random.randrange(400,980)

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


	#if event.type == pygame.KEYDOWN:
	keys=pygame.key.get_pressed()
	if player_x < 1450:
		if keys[pygame.K_RIGHT]:
			if x_acceleration < 10:
				x_acceleration += 1
	else:
		if x_acceleration > 0:
			x_acceleration = 0
	
	if player_x > 400:
		if keys[pygame.K_LEFT]:
			if x_acceleration > -10:
				x_acceleration -=1
	else:
		if x_acceleration < 0:
			x_acceleration = 0

	if player_y < 980:
		if keys[pygame.K_DOWN]:
			if y_acceleration < 10:
				y_acceleration += 1
	else:
		if y_acceleration > 0:
			y_acceleration = 0

	if player_y > 400:
		if keys[pygame.K_UP]:
			if y_acceleration > -10:
				y_acceleration -=1
	else:
		if y_acceleration < 0:
			y_acceleration = 0

	
	player_x += x_acceleration
	player_y += y_acceleration

	screen.fill(Black)
	pygame.draw.rect(screen,White,[400,400,1120,580],2)
	pygame.draw.rect(screen,White,[player_x,player_y,70,70])
 	#pygame.draw.line(screen,White,[projectile_x,projectile_y],[projectile_x + 2,projectile_y + 2],2)
	if player_health < 1:
		screen.fill(Black)
	pygame.display.flip()		                 

	clock.tick(60)
pygame.quit()