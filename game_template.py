import pygame
import random
pygame.init()

# The value for colors
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)
Gray = (108,109,105)

PI = 3.141592653

#the variables of the game
health = 100
rect_x = random.randrange(240,1920)
rect_y = random.randrange(0,1080)
rect_change_x = 25
rect_change_y = 0

#creating the window
size = (1920,1080)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("template")
done = False
clock = pygame.time.Clock()

#quitting the window part 1
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			screen.fill(Black)
			done = True

	#Drawing on the window
	screen.fill(Black)
	pygame.draw.rect(screen,Gray,[0,0,240,1080])
	pygame.draw.line(screen,White,[100,40],[health+100,40],10)
	pygame.draw.rect(screen,White,[20,20,70,70],7)
	font = pygame.font.SysFont('Calibri',25,True,False)
	text = font.render("Player",True,White)
	screen.blit(text,[95,60])
	pygame.draw.rect(screen, Red, [rect_x,rect_y,10,5])
	rect_x += rect_change_x
	rect_y += rect_change_y
	rect_change_x -= 0.2
	rect_change_y += 0.05
	#if rect_change_x < 1:
		#rect_change_x = 0
		#rect_change_y = 0
	#if rect_change_y > 4:
		#rect_change_y = 1
	for i in range(50):
	  	x = random.randrange(240, 1920)
	  	y = random.randrange(0, 1080)
	  	pygame.draw.circle(screen, White, [x, y], 2)
	if rect_y > 1030 or rect_y < -50:
		rect_change_y = rect_change_y * -1
	if rect_x > 1870 or rect_x < 190:
		rect_change_x = rect_change_x * -1     
	pygame.display.flip()		                 
	
	#quitting the window part 2
	clock.tick(60)
pygame.quit()