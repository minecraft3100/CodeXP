import pygame
from constantes import *



class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.health = HEALTH
        self.max_health = HEALTH
        self.attack = ATTACK
        self.velocity = VELOCITY
        self.image = pygame.image.load(PATH_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = RESOLUTION_X/2 - self.rect.width/2
        self.rect.y = 550
    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
