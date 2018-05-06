import pygame
from pygame.locals import*
img = pygame.image.load('soul sprite.png')
img = pygame.transform.scale(img,(70,70))
import random
import time
import sys


class Game:
	def __init__(self, config):
		self.config = config

	def run(self):
		pygame.init()
		self.start_time = time.time()
		self.total_time = -1
		self.Black = (0,0,0)
		self.White = (255,255,255)


		self.boundary_x = 400
		self.boundary_y = 400
		self.boundary_length = 1120
		self.boundary_height = 580
		self.boundary_right = self.boundary_x + self.boundary_length

		self.player_health = (100)
		self.player_x = (700)
		self.player_y = (700)
		self.player = (self.player_x, self.player_y, self.player_health)
		self.player_health_deduction = 1

		self.projectiles = []	
		self.hit_box = pygame.Rect(self.player_x, self.player_y, 70, 70)

		self.ScreenWidth = 1920
		self.ScreenHeight = 1080
		self.size = (self.ScreenWidth, self.ScreenHeight)
		self.screen = pygame.display.set_mode(self.size) 
		pygame.display.set_caption("underfail demo")
		self.clock = pygame.time.Clock()
		self.y_acceleration = 0
		self.x_acceleration = 0
		self.font = pygame.font.SysFont('Calibri', 25, True, False)
		self.gameover_font = pygame.font.SysFont('Calibri', 50, True, False)
		
		self.configeration = ()

		self.loop()

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.screen.fill(self.Black)
				self.done = True
				sys.exit()

			if event.type == pygame.KEYUP:
				self.x_acceleration = 0
				self.y_acceleration = 0


		#if event.type == pygame.KEYDOWN:
		keys=pygame.key.get_pressed()
		if self.hit_box.x < 1445:
			if keys[pygame.K_RIGHT]:
				if self.x_acceleration < 10:
					self.x_acceleration += 1
		else:
			if self.x_acceleration > 0:
				self.x_acceleration = 0
		
		if self.hit_box.x > 405:
			if keys[pygame.K_LEFT]:
				if self.x_acceleration > -10:
					self.x_acceleration -=1
		else:
			if self.x_acceleration < 0:
				self.x_acceleration = 0

		if self.hit_box.y < 900:
			if keys[pygame.K_DOWN]:
				if self.y_acceleration < 10:
					self.y_acceleration += 1
		else:
			if self.y_acceleration > 0:
				self.y_acceleration = 0

		if self.hit_box.y > 410:
			if keys[pygame.K_UP]:
				if self.y_acceleration > -10:
					self.y_acceleration -=1
		else:
			if self.y_acceleration < 0:
				self.y_acceleration = 0

		if self.player_health < 1:
			if keys[pygame.K_SPACE]:
				self.done =True

	def update_projectiles(self):
		# Loop through the projectiles and do stuff
		for projectile in self.projectiles:
			if projectile['x'] >= self.boundary_right:
				self.projectiles.remove(projectile)
			else:
				projectile['x'] = projectile['x'] + 10
			if self.hit_box.collidepoint(projectile['x'], projectile['y']):
				self.player_health -= self.player_health_deduction

	def update_player_health(self):
		if self.player_health < 1 and self.total_time == -1:
			self.total_time = self.time_elapsed

		if self.player_health < 1:
			self.screen.fill(self.Black)
			time_string = time.strftime("%M:%S", time.gmtime(self.total_time))
			timetext = self.gameover_font.render(time_string, True, self.White)
			timetext_size = self.gameover_font.size(time_string)
			self.screen.blit(timetext,[(self.ScreenWidth/2)-timetext_size[0]/2,250])

	def draw_health(self):

		text = self.font.render("HEALTH",True, self.White)
		pygame.draw.rect(self.screen, self.White, [350, 250, self.player_health, 20])
		self.screen.blit(text,[250,250])

	def timer(self):		
		self.time_elapsed = time.time() - self.start_time
		timetext = self.font.render(time.strftime("%M:%S", time.gmtime(self.time_elapsed)),True, self.White)
		self.screen.blit(timetext,[1250,250])

	def drawing(self):		
		self.screen.fill(self.Black)
		self.draw_health()

		pygame.draw.rect(self.screen, self.White, [400,400, self.boundary_length, self.boundary_height],2)

		for projectile in self.projectiles:
			pygame.draw.line( self.screen, self.White,
				[projectile['x'], projectile['y']], [projectile['x'] - 30, projectile['y'] ])
		self.screen.blit(img,(self.hit_box))
	



	def loop(self):
		self.done = False
		while not self.done:

			self.handle_events()

			
			self.hit_box.x += self.x_acceleration
			self.hit_box.y += self.y_acceleration

			if random.randint(0,9) == 0 and len(self.projectiles) < self.config['max_projectiles']:
				self.projectiles.append({'x': random.randrange(400,450), 'y': random.randrange(400,980)})

		
			self.update_projectiles()
			self.drawing()
			self.timer()
			self.update_player_health()

			pygame.display.flip()

			self.clock.tick(60)

class Menu:
	def run(self):
		#do something

		self.Black = (0,0,0)
		self.White = (255,255,255)
		self.selected_config = 'easy'
		self.button_width = 300
		self.button_height = 300
		self.easy_button_rect = pygame.Rect(50, 50, self.button_width, self.button_height)
		self.hard_button_rect = pygame.Rect(450, 50, self.button_width, self.button_height)

		self.ScreenWidth = 1920
		self.ScreenHeight = 1080
		self.size = (self.ScreenWidth, self.ScreenHeight)

		pygame.init()
		self.font = pygame.font.SysFont('Calibri', 25, True, False)
		self.screen = pygame.display.set_mode(self.size) 
		self.clock = pygame.time.Clock()
		self.loop()

	def config(self):
		easy_config = {
			'player_health_deduction': 3,
			'max_projectiles': 10
		}

		hard_config = {
			'player_health_deduction': 5,
			'max_projectiles': 20
		}
		# decide which config to return
		if self.selected_config == 'easy':
			return easy_config
		else:
			if self.selected_config == 'hard':
				return hard_config

	def mouse_interation(self):
		self.ev = pygame.event.get()
		for event in self.ev:
			if event.type == pygame.QUIT:
				sys.exit()			
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if self.easy_button_rect.collidepoint(pos):
					self.done = True
					self.selected_config = 'easy'
				if self.hard_button_rect.collidepoint(pos):
					self.done = True
					self.selected_config = 'hard'

	def drawing(self):		
		self.screen.fill(self.Black)


		pygame.draw.rect(self.screen, self.White, self.easy_button_rect,2)
		pygame.draw.rect(self.screen, self.White, self.hard_button_rect,2)

		easy_text = self.font.render("Easy",True, self.White)
		hard_text = self.font.render("Hard",True, self.White)
		self.screen.blit(easy_text,[300,300])
		self.screen.blit(hard_text,[1620,300])


	def loop(self):
		self.done = False
		while not self.done:

			self.mouse_interation()

			self.drawing()

			pygame.display.flip()

			self.clock.tick(60)





while True:
	underfail_menu = Menu()
	underfail_menu.run()

	config = underfail_menu.config()

	underfail_game = Game(config)
	underfail_game.run()



























