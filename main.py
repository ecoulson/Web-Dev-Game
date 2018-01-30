import pygame
from enemy_maker import enemy_maker
from InvaderSheet import InvaderSheet
from InvaderSheet import Sprites

pygame.init()

BLACK = (0,0,0)

size = (720, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("WebDev Python and Git Practice")
sheet = InvaderSheet()

running = True
clock = pygame.time.Clock()
enemy_manager = enemy_maker(screen)
last = pygame.time.get_ticks()

def render(image, pos):
	width = image.get_width()
	height = image.get_height()
	size = [int(64 * (width / height)), int(64 * (height / width))]
	scaled_image = pygame.transform.scale(image, (size[0], size[1]))
	screen.blit(scaled_image, pos)

while running:
	now = pygame.time.get_ticks()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill(WHITE)
	
	enemy_manager.move()
	if now - last > 3000 :
		enemy_manager.startEnemy()
		last = now
		
	screen.fill(BLACK)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
