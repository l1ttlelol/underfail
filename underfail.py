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

projectiles = []

hit_box = pygame.Rect(player_x,player_y,70,70)
player_health_deduction = 1

size = (1920,1080)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("underfail")
done = False
clock = pygame.time.Clock()
y_acceleration = 0
x_acceleration = 0
font = pygame.font.SysFont('Calibri', 25, True, False)
			
while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			screen.fill(Black)
			done = True


	#if event.type == pygame.KEYDOWN:
	keys=pygame.key.get_pressed()
	if hit_box.x < 1445:
		if keys[pygame.K_RIGHT]:
			if x_acceleration < 10:
				x_acceleration += 1
	else:
		if x_acceleration > 0:
			x_acceleration = 0
	
	if hit_box.x > 405:
		if keys[pygame.K_LEFT]:
			if x_acceleration > -10:
				x_acceleration -=1
	else:
		if x_acceleration < 0:
			x_acceleration = 0

	if hit_box.y < 900:
		if keys[pygame.K_DOWN]:
			if y_acceleration < 10:
				y_acceleration += 1
	else:
		if y_acceleration > 0:
			y_acceleration = 0

	if hit_box.y > 410:
		if keys[pygame.K_UP]:
			if y_acceleration > -10:
				y_acceleration -=1
	else:
		if y_acceleration < 0:
			y_acceleration = 0
	if event.type == pygame.KEYUP:
		x_acceleration = 0
		y_acceleration = 0

	
	hit_box.x += x_acceleration
	hit_box.y += y_acceleration

	if random.randint(0,9) == 0 and len(projectiles) < 10:
		projectiles.append({'x': random.randrange(400,450), 'y': random.randrange(400,980)})

	screen.fill(Black)
	text = font.render("HEALTH",True,White)
	pygame.draw.rect(screen,White,[350,250,player_health,20])
	screen.blit(text,[250,250])
	pygame.draw.rect(screen,White,[400,400,1120,580],2)
	pygame.draw.rect(screen,White,hit_box)
	

	# Loop through the projectiles and do stuff
	for projectile in projectiles:
		pygame.draw.line( screen,White,
			[projectile['x'], projectile['y']], [projectile['x'] - 30, projectile['y'] ])
		if projectile['x'] >= 1520:
			projectiles.remove(projectile)
		else:
			projectile['x'] = projectile['x'] + 10
		if hit_box.collidepoint(projectile['x'], projectile['y']):
			player_health -= player_health_deduction


	if player_health < 1:
		screen.fill(Black)
	pygame.display.flip()

	clock.tick(60)
pygame.quit()