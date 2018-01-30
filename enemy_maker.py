import pygame
import time
from enemy import enemy
class enemy_maker():
    def __init__(self,screen):
        self.screen = screen
        self.enemies = []
    def startEnemy(self):
        e = enemy()
        self.enemies.append(e)
        e.draw(self.screen)
    def move(self):
        for x in self.enemies:
            x.move(self.screen)
