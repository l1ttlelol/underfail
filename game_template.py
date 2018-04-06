import pygame
pygame.init()

# The value for colors
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)

PI = 3.141592653

#the variables of the game
health = 100

#creating the window
size = (700,500)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("template")
quit = False
clock = pygame.time.Clock()

#quitting the window part 1
while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			screen.fill(Black)
			quit = True

	#Drawing on the window
	screen.fill(Black)
	#pygame.draw.line(screen,White,[100,40],[health+100,40],10)
	#pygame.draw.rect(screen,White,[20,20,70,70],7)
	#font = pygame.font.SysFont('Calibri',25,True,False)
	#text = font.render("Player",True,White)
	#screen.blit(text,[95,60])
	pygame.draw.rect(screen, Red, [40,130,20,10])
	pygame.display.flip()		                 
	
	#quitting the window part 2
	clock.tick(60)
pygame.quit()