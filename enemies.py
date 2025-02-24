import pygame
import random
from sounds import *
from damagetext import *
from constants import *
from globals import screen

#Enemy class
class Goomba():
    def __init__(self, x, y, name, max_hp, strength,):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 90

        #*2.5 for bowser
        #load images for idle
        temp_list = []
        for i in range (8):
            image = pygame.image.load(f'images/Enemy/Goomba/Idle/i{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.9, image.get_height() * 0.9))            
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for attack
        temp_list = []
        for i in range (8):
            image = pygame.image.load(f'images/Enemy/Goomba/Attack/a{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.9, image.get_height() * 0.9))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
         #load images for hurt
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/Goomba/Hurt/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.9, image.get_height() * 0.9))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

         #load images for dead (same as hurt)
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/Goomba/Hurt/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.9, image.get_height() * 0.9))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

    def idle(self):
        #set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 90
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def hurt(self):
        if self.hp > 0:
            self.action = 2
        else:
            self.dead()
        self.animation_cooldown = 80
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def dead(self):
        self.animation_cooldown = 80
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def update(self):
            #handle animation
            #update image
            self.image = self.animation_list[self.action][self.frame_index]
            #check if enough time has passed since last update
            if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            
            if self.action == 1 and self.frame_index == 5:
                self.target.ouch() 

            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()

    def draw(self):
        from main import screen
        screen.blit(self.image, self.rect)

class Koopea():
    def __init__(self, x, y, name, max_hp, strength,):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 90

        #*2.5 for bowser
        #load images for idle
        temp_list = []
        for i in range (14):
            image = pygame.image.load(f'images/Enemy/Koopea/Idle/i{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for attack
        temp_list = []
        for i in range (25):
            image = pygame.image.load(f'images/Enemy/Koopea/Attack/a{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
         #load images for hurt
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/Koopea/Hurt/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

         #load images for dead (same as hurt)
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/Koopea/Hurt/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for healing 
        temp_list = []
        for i in range (39):
            image = pygame.image.load(f'images/Enemy/Koopea/Heal/r{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

    def idle(self):
        #set variables to idle animation
        self.animation_cooldown = 80
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 40
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def hurt(self):
        self.animation_cooldown = 80
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def dead(self):
        self.animation_cooldown = 80
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def heal(self):
        self.animation_cooldown = 50
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self):
            #handle animation
            #update image
            self.image = self.animation_list[self.action][self.frame_index]
            #check if enough time has passed since last update
            if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            
            if self.action == 1 and self.frame_index == 15:
                self.target.ouch() 

            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()

    def draw(self):
        from main import screen
        screen.blit(self.image, self.rect)

class HammerBro():
    def __init__(self, x, y, name, max_hp, strength,):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 90

        #*2.5 for bowser
        #load images for idle
        temp_list = []
        for i in range (10):
            image = pygame.image.load(f'images/Enemy/HammerBro/Idle/i{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.65, image.get_height() * 0.65))            
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for attack
        temp_list = []
        for i in range (29):
            image = pygame.image.load(f'images/Enemy/HammerBro/Attack/a{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.65, image.get_height() * 0.65))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
         #load images for hurt
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/HammerBro/Hurt/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.65, image.get_height() * 0.65))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

         #load images for dead (same as hurt)
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/HammerBro/Hurt/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 0.65, image.get_height() * 0.65))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

    def idle(self):
        #set variables to idle animation
        self.action = 0
        self.animation_cooldown = 85
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()            
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 20
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def hurt(self):
        self.animation_cooldown = 80
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def dead(self):
        self.animation_cooldown = 80
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def update(self):
            #handle animation
            #update image
            self.image = self.animation_list[self.action][self.frame_index]
            #check if enough time has passed since last update
            if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            
            if self.action == 1 and self.frame_index == 22:
                self.target.ouch() 

            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.animation_cooldown = 60
                    self.idle()

    def draw(self):
        from main import screen
        screen.blit(self.image, self.rect)

class BowserJr():
    def __init__(self, x, y, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 90

        #*2.5 for bowser
        #load images for idle
        temp_list = []
        for i in range (12):
            image = pygame.image.load(f'images/Enemy/BowserJr/Idle/i{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for fire breath
        temp_list = []
        for i in range (27):
            image = pygame.image.load(f'images/Enemy/BowserJr/Fire/fb{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
        #load images for ground pound
        temp_list = []
        for i in range (32):
            image = pygame.image.load(f'images/Enemy/BowserJr/GroundPound/gp{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for healing 
        temp_list = []
        for i in range (24):
            image = pygame.image.load(f'images/Enemy/BowserJr/Heal/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

         #load images for hurt
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/BowserJr/Hurt/o{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

         #load images for dead
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Enemy/BowserJr/Dead/d{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 3.5, image.get_height() * 3.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

    def idle(self):
        #set variables to idle animation
        self.animation_cooldown = 80
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def firebreath(self, target):
        #deal damage to enemy
        rand = random.randint(-2, 10)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 40
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def groundpound(self, target):
        #deal damage to enemy
        rand = random.randint(-3, 8)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 30
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def heal(self):
        self.animation_cooldown = 50
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.animation_cooldown = 80
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def dead(self):
        self.animation_cooldown = 80
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self):
            #handle animation
            #update image
            self.image = self.animation_list[self.action][self.frame_index]
            #check if enough time has passed since last update
            if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            
            if self.action == 1 and self.frame_index == 15:
                self.target.ouch() 
            elif self.action == 2 and self.frame_index == 32:
                self.target.ouch()

            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 5:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()

    def draw(self):
        from main import screen
        screen.blit(self.image, self.rect)

class Bowser():
    def __init__(self, x, y, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 80

        #load images for idle
        temp_list = []
        for i in range (40):
            image = pygame.image.load(f'images/Bowser/Idle/i{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for fire breath
        temp_list = []
        for i in range (31):
            image = pygame.image.load(f'images/Bowser/Flame/fb{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
        #load images for punch
        temp_list = []
        for i in range (35):
            image = pygame.image.load(f'images/Bowser/Punch/p{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for spin
        temp_list = []
        for i in range (43):
            image = pygame.image.load(f'images/Bowser/Spin/s{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))            
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for healing 
        temp_list = []
        for i in range (39):
            image = pygame.image.load(f'images/Bowser/Heal/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

         #load images for hurt
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/Bowser/Hurt/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

         #load images for dead
        temp_list = []
        for i in range (14):
            image = pygame.image.load(f'images/Bowser/Dead/d{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))  
            temp_list.append(image)
        self.animation_list.append(temp_list)

    def idle(self):
        #set variables to idle animation
        self.animation_cooldown = 80
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def firebreath(self, target):
        #deal damage to enemy
        rand = random.randint(0, 15)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 50
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def punch(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 10)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 50
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def spin(self, target):
        #deal damage to enemy
        rand = random.randint(-3, 12)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()
            gameover()
        damage_text = DamageText(target.rect.centerx, target.rect.y + 150, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.animation_cooldown = 30
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def heal(self):
        self.animation_cooldown = 50
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.animation_cooldown = 80
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def dead(self):
        self.animation_cooldown = 80
        self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self):
            #handle animation
            #update image
            self.image = self.animation_list[self.action][self.frame_index]
            #check if enough time has passed since last update
            if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            
            if self.action == 1 and self.frame_index == 15:
                self.target.ouch() 
            elif self.action == 2 and self.frame_index == 29:
                self.target.ouch()
            elif self.action == 3 and self.frame_index == 23:
                self.target.ouch()

            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 6:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()

    def draw(self):

        screen.blit(self.image, self.rect)


enemy1 = Goomba(750, 345, 'Goomba', 25, 5)
enemy2 = Goomba(845, 415, 'Goomba', 25, 5)

enemy3 = HammerBro(730, 305, 'Hammer Bro', 40, 10)
enemy4 = HammerBro(855, 390, 'Hammer Bro', 40, 10)

enemy5 = Koopea(710, 175, 'Koopea', 30, 7)
enemy6 = Koopea(855, 235, 'Koopea', 30, 7)

enemy7 = Goomba(750, 345, 'Goomba', 30, 7)
enemy8 = HammerBro(855, 235, 'Hammer Bro', 45, 13)
enemy9 = Koopea(920, 285, 'Koopea', 35, 10)

enemy10 = BowserJr(760, 275, 'Bowser Jr.', 150, 15)

enemy11 = Bowser(600, 275, 'Bowser', 250, 20)



enemy_list_lvl1 = []
enemy_list_lvl1.append(enemy1)
enemy_list_lvl1.append(enemy2)

enemy_list_lvl2 = []
enemy_list_lvl2.append(enemy3)
enemy_list_lvl2.append(enemy4)

enemy_list_lvl3 = []
enemy_list_lvl3.append(enemy5)
enemy_list_lvl3.append(enemy6)

enemy_list_lvl4 = []
enemy_list_lvl4.append(enemy7)
enemy_list_lvl4.append(enemy8)
enemy_list_lvl4.append(enemy9)

enemy_list_lvl5 = []
enemy_list_lvl5.append(enemy10)

enemy_list_lvl6 = []
enemy_list_lvl6.append(enemy11)