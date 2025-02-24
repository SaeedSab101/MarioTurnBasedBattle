import pygame
from globals import *

class levelUp():
    def __init__(self, x, y):
        self.animation_list = []
        self.frame_index = 0
        self.action = 1  # Start with levelup2 (animation index 1)
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 70

        temp_list = []
        for i in range(12):  
            image = pygame.image.load(f'images/Mario/LevelUp/LevelUp2/levelup{i}.png')
            image = pygame.transform.scale(image, (1200, 800))
            temp_list.append(image)
        self.animation_list.append(temp_list) 

        temp_list = []
        for i in range(24):  
            image = pygame.image.load(f'images/Mario/LevelUp/levelup{i}.png')
            image = pygame.transform.scale(image, (1200, 800))
            temp_list.append(image)
        self.animation_list.append(temp_list)  

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def levelup(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def levelup2(self):
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self):
        self.image = self.animation_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 1:  
                self.levelup()  
            else:  
                self.frame_index = 0  


    def draw(self):
        screen.blit(self.image, self.rect)