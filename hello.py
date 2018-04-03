import pygame
pygame.init()

# The value for colors
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)

PI = 3.14159265

#creating the window
size = (700,500)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("practice")
done = False
clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True                 
	pygame.display.flip()
	clock.tick(60)
pygame.quit()
