import pygame
RED = (255,0,0)
class enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = 0
		self.y = 0
		self.NO_U = 1
		

	def draw(self,screen):
		pygame.draw.rect(screen, RED, [self.x, self.y, 50, 50])
		

	def move(self,screen):
		
		self.x = self.x + (5*self.NO_U)
		if self.x == 650 or self.x <0 :
			self.y = self.y + 50
			self.NO_U = self.NO_U * -1
		self.draw(screen)






# #mine

# import pygame
# def spawn():
	
# RED = (255,0,0)
# self.x = 0
# y = 0
# clock = pygame.time.Clock()
# while running:
# 	pygame.draw.rect(screen, RED, [self.x, y, 50, 50])
# 	pygame.display.flip()
# 	self.x = self.x + 5
# 	if self.x = 650 :
# 		y = y + 15
# 	clock.tick(60)
