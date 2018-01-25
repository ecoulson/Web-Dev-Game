import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("WebDev Python and Git Practice")

running = True
clock = pygame.time.Clock()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill(WHITE)
	pygame.display.flip()
	clock.tick(60)

pygame.quit()