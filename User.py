import pygame
import random
import block_library
	
		
class Player(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		super().__init__()
		
		self.image = pygame.image.load("Michael_Simpson.jpg").convert()
		self.image.set_colorkey(WHITE)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rect.width = self.image.get_width()
		self.rect.height = self.image.get_height()

		self.change_x = 0
		self.change_y = 0
		
		
	def set_speed(self, x, y):
		self.change_x = x
		self.change_y = y
		
		
	def update(self, screen_width, screen_height):
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		
		if self.rect.x > (screen_width - self.rect.width):
			self.rect.x = screen_width - self.rect.width
			off_screen_sound.play()
			
		if self.rect.x < 0:
			self.rect.x = 0
			off_screen_sound.play()
			
		if self.rect.y > (screen_height -  self.rect.height):
			self.rect.y = screen_height - self.rect.height
			off_screen_sound.play()
			
		if self.rect.y < 0:
			self.rect.y = 0
			off_screen_sound.play()
		
		
class Score(): 
	def __init__(self):
		self.score = 0
		self.color = BLACK
	
	
	def adjust(self, amount):
		self.score += amount
		
	def draw(self, screen):
		if self.score == 0:
			self.color = BLACK
			
		if self.score < 0:
			self.color = RED
			
		if self.score > 0:
			self.color = GREEN
		
		pygame.draw.rect(screen, WHITE, [0, 0, 90, 90])
		pygame.draw.rect(screen, score.color, [0, 0, 90, 90], 3)
		
		font = pygame.font.SysFont('Comic_Sans_MS', 40, False, True)
		text = font.render(str(self.score), True, self.color)
		screen.blit(text, [30, 30])        

user = User(screen[0], screen[1])
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
bad_block_sound = pygame.mixer.Sound("bad_block.wav")
good_block_sound = pygame.mixer.Sound("good_block.wav")
off_screen_sound = pygame.mixer.Sound("bump.wav")
all_sprites_list.update(screen_width, screen_height)
all_sprites_list.draw(screen)

elif event.type == pygame.KEYDOWN:
	if event.key == pygame.K_w:
		player.set_speed(player.change_x, -3)
	if event.key == pygame.K_a:
		player.set_speed(-3, player.change_y)
	if event.key == pygame.K_s:
		player.set_speed(player.change_x, 3)
	if event.key == pygame.K_d:
		player.set_speed(3, player.change_y)
		
elif event.type == pygame.KEYUP:
	if event.key == pygame.K_w:
		player.set_speed(player.change_x, 0)
	if event.key == pygame.K_a:
		player.set_speed(0, player.change_y) 
	if event.key == pygame.K_s:
		player.set_speed(player.change_x, 0)
	if event.key == pygame.K_d:
		player.set_speed(0, player.change_y)