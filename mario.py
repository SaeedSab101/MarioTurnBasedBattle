import pygame
from sounds import *
from damagetext import *
from constants import *
from globals import screen


class Mario():
    def __init__(self, x, y, name, max_hp, max_fp, strength, mushrooms, syrups, superMushrooms):
        self.x = x
        self.y = y
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_fp = max_fp
        self.fp = max_fp
        self.strength = strength
        self.start_mushrooms = mushrooms
        self.mushrooms = mushrooms
        self.superMushrooms = superMushrooms
        self.start_syrups = syrups
        self.syrups = syrups
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 90
        self.timer = 3
        self.attack_sound_played = False  # Flag to track if marioAttack1() has been played


        #load images for idle
        temp_list = []
        for i in range (8):
            image = pygame.image.load(f'images/{self.name}/Idle/i{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for jump
        temp_list = []
        for i in range (20):
            image = pygame.image.load(f'images/{self.name}/Jump/j{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for hammer
        temp_list = []
        for i in range (22):
            image = pygame.image.load(f'images/{self.name}/Hammer/h{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for spin
        temp_list = []
        for i in range (24):
            image = pygame.image.load(f'images/{self.name}/Spin/s{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for fire
        temp_list = []
        for i in range (14):
            image = pygame.image.load(f'images/{self.name}/Fire/f{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for mushroom
        temp_list = []
        for i in range (35):
            image = pygame.image.load(f'images/{self.name}/Mushroom/m{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load images for syrup
        temp_list = []
        for i in range (35):
            image = pygame.image.load(f'images/{self.name}/Syrup/sy{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2))                  
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
        #load images for hurt
        temp_list = []
        for i in range (6):
            image = pygame.image.load(f'images/{self.name}/Ouch/o{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for dead
        temp_list = []
        for i in range (20):
            image = pygame.image.load(f'images/{self.name}/Dead/d{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #load different win animations
        temp_list = []
        for i in range (14):
            image = pygame.image.load(f'images/{self.name}/Win/WinJ/w{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        temp_list = []
        for i in range (14):
            image = pygame.image.load(f'images/{self.name}/Win/WinH/w{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        temp_list = []
        for i in range (14):
            image = pygame.image.load(f'images/{self.name}/Win/WinS/w{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        temp_list = []
        for i in range (14):
            image = pygame.image.load(f'images/{self.name}/Win/WinF/w{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
   
        #load images for idle
        temp_list = []
        for i in range (12):
            image = pygame.image.load(f'images/{self.name}/IdleTurn/id{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for super mushroom
        temp_list = []
        for i in range (35):
            image = pygame.image.load(f'images/{self.name}/SuperMushroom/sm{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2)) 
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def idle(self): 
        #set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def jump(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 40

    def hammer(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 10)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 40

    def spin(self, target):
        #deal damage to enemy
        rand = random.randint(0, 15)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        
        #set variables to attack animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 50

    def fire(self, target):
        #deal damage to enemy
        rand = random.randint(0, 20)
        damage = self.strength + rand
        target.hp -= damage
        self.target = target
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        #set variables to attack animation
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 80
        
    def mushroom(self):
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 50

    def syrup(self):
        self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 50

    def ouch(self):
        if self.hp > 0:
            self.action = 7
        else:
            self.dead()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        marioHit()

    def dead(self):
        self.action = 8
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 50
    
    def win1(self):
        self.action = 9
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 80

    def win2(self):
        self.action = 10
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 80

    def win3(self):
        self.action = 11
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 80

    def win4(self):
        self.action = 12
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 80
   
    def idleTurn(self):
        self.action = 13
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 50

    def superMushroom(self):
        self.action = 14
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 50

    def update(self):
        # Handle animation
        # Update image
        self.image = self.animation_list[self.action][self.frame_index]
        
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        def checkIfDead():
            if self.target.hp <= 0:
                self.target.dead()
            else:
                self.target.hurt() 
                enemyHit()

        if self.action == 1 and self.frame_index == 0 and not self.attack_sound_played:
            marioAttack1()
            self.attack_sound_played = True 
        if self.action == 1 and self.frame_index == 13:
            checkIfDead()
            marioAttack2()
            self.attack_sound_played = False  

        elif self.action == 2 and self.frame_index == 0:
            marioAttack1()
            self.attack_sound_played = True 
        if self.action == 2 and self.frame_index == 12:
            checkIfDead()
            marioAttack2()
            self.attack_sound_played = False  

        elif self.action == 3 and self.frame_index == 15:
            self.target.hurt() 
            checkIfDead()
        if self.action == 4 and self.frame_index == 12:
            self.target.hurt() 
            checkIfDead()
        
        # If the animation has run out, handle it based on the action
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action in {8, 9, 10, 11, 12}:  # Win animations
                # Freeze at the last frame of the win animation
                self.frame_index = len(self.animation_list[self.action]) - 1
            elif self.action in {1, 2, 3, 4, 5, 6}:  # Attack animations
                # Return to idle after attack animations
                self.frame_index = 0
                self.action = 0
            elif self.action == 13 and not win_animation_started:  # Idle turn (only if win animation is not active)
                self.idleTurn()
                self.frame_index = 0
            else:
                # Default behavior: return to idle
                self.animation_cooldown = 90
                self.idle()

    def draw(self):
        screen.blit(self.image, self.rect)

win_animation_started = False
win_animation_time = 0

def winAnimation(enemy_list):
    global win_animation_started, win_animation_time

    if all(not enemy.alive for enemy in enemy_list):  
        if not win_animation_started:
            win_animation_started = True
            win_animation_time = pygame.time.get_ticks()  # Record start time

        current_time = pygame.time.get_ticks()  # Get current time
        elapsed_time = current_time - win_animation_time  # Time since animation started

        if elapsed_time > 1000 and elapsed_time <= 3000:  # Play win animation within 1-3 seconds
            if mario.action == 0:  
                mario.win1()
            elif mario.action == 2:  
                mario.win2()
            elif mario.action == 3: 
                mario.win3()
            elif mario.action == 4:  
                mario.win4()
        elif elapsed_time > 3000:  # Animation complete
            win_animation_started = False  # Reset animation state
            win_animation_time = 0 

mario = Mario(440, 270, 'Mario', 100, 25, 10, 3, 3, 0)
