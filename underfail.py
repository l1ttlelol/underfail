import pygame
import random
import time
pygame.init()

start_time = time.time()
total_time = -1


Black = (0,0,0)
White = (255,255,255)
ScreenWidth = 1920
ScreenHeight = 1080


boundary_x = 400
boundary_y = 400
boundary_length = 1120
boundary_height = 580
boundary_right = boundary_x + boundary_length

player_health = (100)
player_x = (700)
player_y = (700)
player = (player_x,player_y,player_health)

projectiles = []

hit_box = pygame.Rect(player_x,player_y,70,70)
player_health_deduction = 3

size = (ScreenWidth,ScreenHeight)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("underfail")
done = False
clock = pygame.time.Clock()
y_acceleration = 0
x_acceleration = 0
font = pygame.font.SysFont('Calibri', 25, True, False)
gameover_font = pygame.font.SysFont('Calibri', 50, True, False)
			
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

	if random.randint(0,9) == 0 and len(projectiles) < 15:
		projectiles.append({'x': random.randrange(400,450), 'y': random.randrange(400,980)})

	screen.fill(Black)
	text = font.render("HEALTH",True,White)
	pygame.draw.rect(screen,White,[350,250,player_health,20])
	screen.blit(text,[250,250])

	time_elapsed = time.time() - start_time
	timetext = font.render(time.strftime("%M:%S", time.gmtime(time_elapsed)),True,White)
	screen.blit(timetext,[1250,250])

	pygame.draw.rect(screen,White,[400,400, boundary_length, boundary_height],2)
	pygame.draw.rect(screen,White,hit_box)
	

	# Loop through the projectiles and do stuff
	for projectile in projectiles:
		pygame.draw.line( screen,White,
			[projectile['x'], projectile['y']], [projectile['x'] - 30, projectile['y'] ])
		if projectile['x'] >= boundary_right:
			projectiles.remove(projectile)
		else:
			projectile['x'] = projectile['x'] + 10
		if hit_box.collidepoint(projectile['x'], projectile['y']):
			player_health -= player_health_deduction


	if player_health < 1 and total_time == -1:
		total_time = time_elapsed

	if player_health < 1:
		screen.fill(Black)
		time_string = time.strftime("%M:%S", time.gmtime(total_time))
		timetext = gameover_font.render(time_string,True,White)
		timetext_size = gameover_font.size(time_string)
		screen.blit(timetext,[(ScreenWidth/2)-timetext_size[0]/2,250])


	pygame.display.flip()

	clock.tick(60)
pygame.quit()