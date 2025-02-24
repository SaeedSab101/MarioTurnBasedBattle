import pygame
from constants import *

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        from main import target
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        if target and target.name == "Koopea":
            self.rect.center = (x, y + 250)  # Increase y by 250
        else:
            self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        #move damage text up
        self.rect.y -= 1
        #delete the text after a few seconds
        self.counter += 1
        if self.counter > 30:
            self.kill()

damage_text_group = pygame.sprite.Group()