import pygame
import random
import tkinter as tk
import pyglet
import time

#import custom font
fontName = "fonts/SuperMario256.ttf"
fontTarget = "fonts/speechText.ttf"
pyglet.font.add_file(f'{fontName}')
pyglet.font.add_file(f'{fontTarget}')

#import music
from pygame import mixer
mixer.init()

#initialize game
pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_panel = 200
screen_width = 1200
screen_height = 600 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

#define game variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait = 90
attack = False
jump = False
hammer = False
spin = False
fire = False
mushroom = False
mushroom_effect = 35
super_mushroom_effect = 75
syrup = False
syrup_effect = 15
clicked = False

#define fonts
font = pygame.font.Font(fontName, 26)
titleFont = pygame.font.Font(fontName, 40)
font2 = pygame.font.Font(fontTarget, 45)


#define colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 139)

#load images

#main menu background images
menu_img = pygame.image.load('images/Backgrounds/Menu/menu.png').convert_alpha()
scaled_menu_image = pygame.transform.scale(menu_img, (screen_width, screen_height))


#level1 background images
background_img = pygame.image.load('images/Backgrounds/lvl1.png').convert_alpha()
scaled_image = pygame.transform.scale(background_img, (screen_width, screen_height - bottom_panel))

#level2 background images
background_img2 = pygame.image.load('images/Backgrounds/lvl2.png').convert_alpha()
scaled_image2 = pygame.transform.scale(background_img2, (screen_width, screen_height - bottom_panel))

#level3 background images
background_img3 = pygame.image.load('images/Backgrounds/lvl3.png').convert_alpha()
scaled_image3 = pygame.transform.scale(background_img3, (screen_width, screen_height - bottom_panel))

#level4 background images
background_img4 = pygame.image.load('images/Backgrounds/lvl4.png').convert_alpha()
scaled_image4 = pygame.transform.scale(background_img4, (screen_width, screen_height - bottom_panel))

#level5 background images
background_img5 = pygame.image.load('images/Backgrounds/lvl5.png').convert_alpha()
scaled_image5 = pygame.transform.scale(background_img5, (screen_width, screen_height - bottom_panel))

#level6 background images
background_img6 = pygame.image.load('images/Backgrounds/lvl6.png').convert_alpha()
scaled_image6 = pygame.transform.scale(background_img6, (screen_width, screen_height - bottom_panel))

#panel image
panel_img = pygame.image.load('images/Panel.png').convert_alpha()
panel_img1 = pygame.image.load('images/Panels/panelLVL1.png').convert_alpha()
panel_img2 = pygame.image.load('images/Panels/panelLVL2.png').convert_alpha()
panel_img3 = pygame.image.load('images/Panels/panelLVL3.png').convert_alpha()
panel_img4 = pygame.image.load('images/Panels/panelLVL4.png').convert_alpha()
panel_img5 = pygame.image.load('images/Panels/panelLVL5.png').convert_alpha()
panel_img6 = pygame.image.load('images/Panels/panelLVL6.png').convert_alpha()

#mouse image
mouse_img = pygame.image.load('images/pointer.png').convert_alpha()

movesList = pygame.image.load('images/Buttons/moveList.png')
movesList_image = pygame.transform.scale(movesList, (movesList.get_width() * 1.7 , movesList.get_height() * 1.7))

def draw_movesList():
    screen.blit(movesList_image, (0,0))


demoImage = pygame.image.load('images/Demo/demo.png')
demoImage2 = pygame.image.load('images/Demo/demo2.png')
demoImage3 = pygame.image.load('images/Demo/demo3.png')
demoImage4 = pygame.image.load('images/Demo/demo4.png')

def draw_demo():
    screen.blit(demoImage, (100,75))
    draw_text("Select Your Enemy", font, green, 82, 30)
    screen.blit(demoImage2, (475,75))
    draw_text("Select Your Action", font, green, 457, 30)
    screen.blit(demoImage3, (839,75))
    draw_text("Let It Play", font, green, 880, 30)
    screen.blit(demoImage4, (280,390))
    draw_text("FIGHT IT OUT!", font, green, 495, 365)

#create function for drawing text
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_mainmenu():
    screen.blit(scaled_menu_image, (0,0))

#function for drawing background
def draw_lvl1():
    screen.blit(scaled_image, (0,0))

def draw_lvl2():
    screen.blit(scaled_image2, (0,0))

def draw_lvl3():
    screen.blit(scaled_image3, (0,0))

def draw_lvl4():
    screen.blit(scaled_image4, (0,0))

def draw_lvl5():
    screen.blit(scaled_image5, (0,0))

def draw_lvl6():
    screen.blit(scaled_image6, (0,0))

#function for drawing panel
def draw_panel(lvl):
    #draw panel

    screen.blit(panel_img1, (0,600))

    def marioStats():
        #show mario stats
        draw_text(f'{mario.name} HP: {mario.hp}', font, red, 150, 610)
        draw_text(f'{mario.name} FP: {mario.fp}', font, red, 150, 650)
        draw_text(f'Mushrooms: {mario.mushrooms}', font, red, 150, 690)
        draw_text(f'Syrups: {mario.syrups}', font, red, 150, 730)
    
    #loop if multiple enemies
    if lvl == 1:
        marioStats()
        for count, enemy in enumerate(enemy_list_lvl1):
            #show name and health
            draw_text(f'{enemy.name} HP: {enemy.hp}', font, red, 850, (600) + count * 40)

    elif lvl == 2:
        screen.blit(panel_img2, (0,600))
        marioStats()
        for count, enemy in enumerate(enemy_list_lvl2):
            #show name and health
            draw_text(f'{enemy.name} HP: {enemy.hp}', font, red, 850, (600) + count * 40)
    
    elif lvl == 3:
        screen.blit(panel_img3, (0,600))
        marioStats()
        for count, enemy in enumerate(enemy_list_lvl3):
            #show name and health
            draw_text(f'{enemy.name} HP: {enemy.hp}', font, red, 853, (600) + count * 40)

    elif lvl == 4:
        screen.blit(panel_img4, (0,600))
        marioStats()
        for count, enemy in enumerate(enemy_list_lvl4):
            #show name and health
            draw_text(f'{enemy.name} HP: {enemy.hp}', font, red, 850, (600) + count * 40)

    elif lvl == 5:
        screen.blit(panel_img5, (0,600))
        marioStats()
        for count, enemy in enumerate(enemy_list_lvl5):
            #show name and health
            draw_text(f'{enemy.name} HP: {enemy.hp}', font, red, 850, (600) + count * 40)

    elif lvl == 6:
        screen.blit(panel_img6, (0,600))
        marioStats()
        for count, enemy in enumerate(enemy_list_lvl6):
            #show name and health
            draw_text(f'{enemy.name} HP: {enemy.hp}', font, red, 880, (600) + count * 40)

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

def enemyHit():
    if not hasattr(enemyHit, "last_played") or pygame.time.get_ticks() - enemyHit.last_played > 500:  # 500ms cooldown
        rand = random.randrange(0, 2)
        if rand == 0:
            enemyHit_sound = mixer.Sound('sfx/enemyHit.mp3')
        elif rand == 1:
            enemyHit_sound = mixer.Sound('sfx/enemyHit1.mp3')
        enemyHit_sound.set_volume(0.5)
        enemyHit_sound.play()
        enemyHit.last_played = pygame.time.get_ticks()  # Update the last played time

def marioAttack1():
    if not hasattr(marioAttack1, "last_played") or pygame.time.get_ticks() - marioAttack1.last_played > 500:  # 500ms cooldown
        rand = random.randrange(0, 2)  # Randomly pick one of 4 sounds
        if rand == 0:
            attack_sound = mixer.Sound('sfx/Mario/Attack/Hammer/h1.wav')
        elif rand == 1:
            attack_sound = mixer.Sound('sfx/Mario/Attack/Hammer/h1-2.wav')
        attack_sound.set_volume(0.3)  # Adjust volume as needed
        attack_sound.play()
        marioAttack1.last_played = pygame.time.get_ticks()  # Update the last played time

def marioAttack2():
    if not hasattr(marioAttack2, "last_played") or pygame.time.get_ticks() - marioAttack2.last_played > 500:  # 500ms cooldown
        rand = random.randrange(0, 2)  # Randomly pick one of 4 sounds
        if rand == 0:
            attack_sound = mixer.Sound('sfx/Mario/Attack/Hammer/h2.wav')
        elif rand == 1:
            attack_sound = mixer.Sound('sfx/Mario/Attack/Hammer/h2-2.wav')
        attack_sound.set_volume(0.3)  # Adjust volume as needed
        attack_sound.play()
        marioAttack2.last_played = pygame.time.get_ticks()  # Update the last played time

def gameover():
    if not hasattr(gameover, "played"):  
        mixer.music.fadeout(500)
        gameover_sound = mixer.Sound('sfx/Mario/Dead/gameover.wav') 
        gameover_sound.set_volume(0.5) 
        gameover_sound.play()
        gameover.played = True 

def marioHit():
    if not hasattr(marioHit, "last_played") or pygame.time.get_ticks() - marioHit.last_played > 500:  # 500ms cooldown
        rand = random.randrange(0, 3)
        if rand == 0:
            marioHit_sound = mixer.Sound('sfx/Mario/Hurt/oof.wav')
        elif rand == 1:
            marioHit_sound = mixer.Sound('sfx/Mario/Hurt/doh.wav')
        elif rand == 2:
            marioHit_sound = mixer.Sound('sfx/Mario/Hurt/eek.wav')
        marioHit_sound.set_volume(0.2)
        marioHit_sound.play()
        marioHit.last_played = pygame.time.get_ticks()  # Update the last played time

def again():
    playAgain = mixer.Sound('sfx/Mario/Restart/again.mp3')
    playAgain.set_volume(0.2)
    playAgain.play()




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

'''class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        #update with new health
        self.hp = hp
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio , 20))
'''

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
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


mario = Mario(440, 270, 'Mario', 100, 25, 10, 3, 3, 0)
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

#itemAni = itemUse(439,275)
levelUP = levelUp(600,400)

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

'''
mario_health_bar = HealthBar(100, 700, mario.hp, mario.max_hp)
enemy_health_bar = HealthBar(700, 700, enemy1.hp, enemy1.max_hp)
enemy_health_bar = HealthBar(700, 800, enemy2.hp, enemy2.max_hp)
'''
play_button = pygame.image.load('images/Buttons/start.png')  # Load button image
play_button_img = pygame.transform.scale(play_button, (play_button.get_width() * 0.8, play_button.get_height() * 0.8))
play_button_rect = play_button_img.get_rect()

info_button = pygame.image.load('images/Buttons/info.png')  # Load button image
info_button_img = pygame.transform.scale(info_button, (info_button.get_width() * 0.8, info_button.get_height() * 0.8))
info_button_rect = info_button_img.get_rect()

back_button = pygame.image.load('images/Buttons/back.png')  # Load button image
back_button_img = pygame.transform.scale(back_button, (back_button.get_width() * 0.5, back_button.get_height() * 0.5))
back_button_rect = back_button_img.get_rect()

next_button = pygame.image.load('images/Buttons/next.png')  # Load button image
next_button_img = pygame.transform.scale(next_button, (next_button.get_width() * 0.5, next_button.get_height() * 0.5))
next_button_rect = next_button_img.get_rect()

level2_button = pygame.image.load('images/Buttons/next.png')  # Load button image
level2_button_img = pygame.transform.scale(level2_button, (level2_button.get_width() * 0.5, level2_button.get_height() * 0.5))
level2_button_rect = level2_button_img.get_rect()

retry_button = pygame.image.load('images/Buttons/retry.png')  # Load button image
retry_button_img = pygame.transform.scale(retry_button, (retry_button.get_width() * 0.5, retry_button.get_height() * 0.5))
retry_button_rect = retry_button_img.get_rect()

# Button settings
jump_button = pygame.image.load('images/Buttons/jumpButton.png')  # Load button image
jump_button_img = pygame.transform.scale(jump_button, (jump_button.get_width() * 2.1, jump_button.get_height() * 2.1))
jump_button_rect = jump_button_img.get_rect()

hammer_button = pygame.image.load('images/Buttons/hammerButton.png')  # Load button image
hammer_button_img = pygame.transform.scale(hammer_button, (hammer_button.get_width() * 2.1, hammer_button.get_height() * 2.1))
hammer_button_rect = hammer_button_img.get_rect()

spin_button = pygame.image.load('images/Buttons/spinButton.png')  # Load button image
spin_button_img = pygame.transform.scale(spin_button, (spin_button.get_width() * 2.1, spin_button.get_height() * 2.1))
spin_button_rect = spin_button_img.get_rect()

fire_button = pygame.image.load('images/Buttons/fireButton.png')  # Load button image
fire_button_img = pygame.transform.scale(fire_button, (fire_button.get_width() * 2.1, fire_button.get_height() * 2.1))
fire_button_rect = fire_button_img.get_rect()

mushroom_button = pygame.image.load('images/Buttons/mushroomButton.png')  # Load button image
mushroom_button_img = pygame.transform.scale(mushroom_button, (mushroom_button.get_width() * 2.1, mushroom_button.get_height() * 2.1))
mushroom_button_rect = mushroom_button_img.get_rect()

syrup_button = pygame.image.load('images/Buttons/syrupButton.png')  # Load button image
syrup_button_img = pygame.transform.scale(syrup_button, (syrup_button.get_width() * 2.1, syrup_button.get_height() * 2.1))
syrup_button_rect = syrup_button_img.get_rect()

super_mushroom_button = pygame.image.load('images/Buttons/superMushroomButton.png')  # Load button image
super_mushroom_button_img = pygame.transform.scale(super_mushroom_button, (super_mushroom_button.get_width() * 2.1, super_mushroom_button.get_height() * 2.1))
super_mushroom_button_rect = super_mushroom_button_img.get_rect()

displayEnemeyName = pygame.image.load('images/targetNameBox.png')  
displayEnemeyName_img = pygame.transform.scale(displayEnemeyName, (displayEnemeyName.get_width() * 2.0, displayEnemeyName.get_height() * 1.2))
def draw_border():
    screen.blit(displayEnemeyName_img, (800, 0))

class Button():
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create button instances
play_button = Button(play_button_img, 400, 500)
info_button = Button(info_button_img, 400, 200)
back_button = Button(back_button_img, 950, 700)
next_button = Button(next_button_img, 950, 700)
level2_button = Button(level2_button_img, 400, 200)
retry_button = Button(retry_button_img, 800, 200)
jump_button = Button(jump_button_img, 450, 600)
hammer_button = Button(hammer_button_img, 550, 600)
spin_button = Button(spin_button_img, 450, 700)
fire_button = Button(fire_button_img, 550, 700)
mush_button = Button(mushroom_button_img, 650, 600)
syrup_button = Button(syrup_button_img, 650, 700)
super_mush_button = Button(super_mushroom_button_img, 750, 650)
back_to_menu_button = Button(back_button_img, 400, 200)


target = None
game_screen = "menu"

def change_music(soundtrack):
    mixer.music.load(f'music/{soundtrack}.mp3')
    mixer.music.play(-1)  # Loop the music indefinitely
    mixer.music.set_volume(0.2)  # Adjust the volume

# Set the initial soundtrack when the game starts
soundtrack = "wonderTitleScreen"
change_music(soundtrack)

def information():
    draw_text("Jump - Does Between 5 and 15 Damage", titleFont, green, 140, 60)
    draw_text("Hammer - Does Between 7 and 18 Damage", titleFont, green, 140, 185)
    draw_text("Special Move - Spin:", titleFont, green, 140, 295)
    draw_text("Does Between 10 and 25 Damage - Uses 4 FP", titleFont, green, 140, 330)
    draw_text("Special Move - Fire:", titleFont, green, 140, 425)
    draw_text("Does Between 10 and 25 Damage - Uses 5 FP", titleFont, green, 140, 460)
    draw_text("Item - Mushroom - Replinishes 35 HP", titleFont, green, 140, 560)
    draw_text("Item - Syrup - Replinishes 15 FP", titleFont, green, 140, 685)


def reset_level(level):
    if hasattr(gameover, "played"):
        delattr(gameover, "played")

    mixer.music.play(-1)

    # Reset Mario's state
    if level == enemy_list_lvl5 or level == enemy_list_lvl6:
        mario.strength = 13
    if level == enemy_list_lvl6:
        mario.superMushrooms = 3
        mario.hp = 150
    mario.hp = mario.max_hp
    mario.fp = mario.max_fp
    mario.mushrooms = mario.start_mushrooms  # Set to the initial number of mushrooms
    mario.syrups = mario.start_syrups  # Set to the initial number of syrups
    mario.alive = True
    mario.action = 0
    mario.frame_index = 0
    # Reset enemies' state
    for enemy in level:
        enemy.hp = enemy.max_hp
        enemy.alive = True
        enemy.action = 0
        enemy.frame_index = 0

    # Reset other game state variables
    global current_fighter, action_cooldown, target
    current_fighter = 1
    action_cooldown = 0
    target = None

    # Reset any other necessary variables or objects
    damage_text_group.empty()  # Clear any damage text

def reset_all_levels():
    mario.max_hp = 100
    reset_level(enemy_list_lvl1)
    reset_level(enemy_list_lvl2)
    reset_level(enemy_list_lvl3)
    reset_level(enemy_list_lvl4)
    reset_level(enemy_list_lvl5)
    reset_level(enemy_list_lvl6)
    if hasattr(gameover, "played"):
        delattr(gameover, "played")


allDead = False
run = True
while run:
    clock.tick(fps)

    pos = pygame.mouse.get_pos()

    def drawUI():
        # Draw buttons and update UI
        jump_button.draw(screen)
        hammer_button.draw(screen)
        spin_button.draw(screen)
        fire_button.draw(screen)
        mush_button.draw(screen)
        syrup_button.draw(screen)
        if game_screen == "level6":
            super_mush_button.draw(screen)
            draw_text(f'Super Mush: {mario.superMushrooms}', font, red, 150, 770)

    def buttonClick(buttons, mario, enemy_list, pos, clicked):
        jump, hammer, spin, fire, mushroom, syrup, superMushroom = False, False, False, False, False, False, False  # Initialize action flags

        for button in buttons:
            if mario.hp > 0 and any(enemy.alive for enemy in enemy_list):
                pygame.mouse.set_visible(False)
                screen.blit(mouse_img, pos)
                if button.is_clicked(pos) and clicked:
                    # Handle button click actions
                    if button == buttons[0]:  # jump_button
                        jump = True
                    elif button == buttons[1]:  # hammer_button
                        hammer = True
                    elif button == buttons[2]:  # spin_button
                        spin = True
                    elif button == buttons[3]:  # fire_button
                        fire = True
                    elif button == buttons[4]:  # mush_button
                        mushroom = True
                    elif button == buttons[5]:  # syrup_button
                        syrup = True
                    elif button == buttons[6]:  # syrup_button
                        superMushroom = True
        return jump, hammer, spin, fire, mushroom, syrup, superMushroom
    
    #handle mario action so that it isnt rewritten each time in a level
    def marioAction(mario, target, current_fighter, action_cooldown, action_wait, jump, hammer, spin, fire, mushroom, syrup, superMushroom, damage_text_group, green):#itemAni
        if current_fighter == 1:
            action_cooldown += 1
            if action_cooldown >= action_wait:
                if allDead == False:
                    mario.action = 13                 
                # Look for player action
                if jump and target and target.alive:
                    mario.action = 1
                    mario.frame_index = 0
                    mario.jump(target)
                    current_fighter += 1
                    action_cooldown = 0
                    target = None
                elif hammer and target and target.alive:
                    mario.action = 2
                    mario.frame_index = 0
                    mario.hammer(target)
                    current_fighter += 1
                    action_cooldown = 0
                    target = None
                elif spin and target and target.alive and mario.fp >= 4:
                    mario.action = 3
                    mario.frame_index = 0
                    mario.spin(target)
                    current_fighter += 1
                    action_cooldown = -20
                    target = None
                    mario.fp -= 4
                elif fire and target and target.alive and mario.fp >= 5:
                    mario.action = 4
                    mario.frame_index = 0
                    mario.fire(target)
                    current_fighter += 1
                    action_cooldown = 0
                    target = None
                    mario.fp -= 5
                elif mushroom:
                    if mario.mushrooms > 0:
                        mario.action = 5
                        mario.frame_index = 0
                        heal_amount = min(mushroom_effect, mario.max_hp - mario.hp)
                        mario.hp += heal_amount
                        mario.mushrooms -= 1
                        damage_text = DamageText(mario.rect.centerx, mario.rect.y + 150, str(heal_amount), green)
                        damage_text_group.add(damage_text)
                        current_fighter += 1
                        action_cooldown = -140
                elif syrup:
                    if mario.syrups > 0:
                        mario.action = 6
                        mario.frame_index = 0
                        fp_regen_amount = min(syrup_effect, mario.max_fp - mario.fp)
                        mario.fp += fp_regen_amount
                        mario.syrups -= 1
                        damage_text = DamageText(mario.rect.centerx, mario.rect.y + 150, str(fp_regen_amount), green)
                        damage_text_group.add(damage_text)
                        current_fighter += 1
                        action_cooldown = -140
                elif superMushroom:
                    if mario.superMushrooms > 0:
                        mario.action = 14
                        mario.frame_index = 0
                        heal_amount = min(super_mushroom_effect, mario.max_hp - mario.hp)
                        mario.hp += heal_amount
                        mario.superMushrooms -= 1
                        damage_text = DamageText(mario.rect.centerx, mario.rect.y, str(heal_amount), green)
                        damage_text_group.add(damage_text)
                        current_fighter += 1
                        action_cooldown = -140
        return current_fighter, action_cooldown, target

    
    
    def targetName(name):
        draw_text(f'Target: {name}', font2, blue, 840, 25)

    def enemySelect():
        enemySelect = mixer.Sound('sfx/enemySelect.WAV')
        enemySelect.set_volume(0.5)
        enemySelect.play()
    
    winPlayed = False

    def levelWin():
        global winPlayed  # Access the global winPlayed flag
        if not winPlayed:  # Check if the sound hasn't been played yet
            mixer.music.stop()  # Stop any other music playing
            winPlay = False
            win = mixer.Sound('sfx/Mario/win.wav')
            win.set_volume(0.2)
            win.play()
            winPlayed = True
        

    if game_screen == "menu":
        #reset_all_levels()
        draw_mainmenu()
        info_button.draw(screen)
        play_button.draw(screen)
        draw_text("Welcome to The Demo!", titleFont, green, 400, 0)

        if info_button.is_clicked(pos) and clicked == True:
            game_screen = "info"
            draw_mainmenu()
            next_button.draw(screen)

        if play_button.is_clicked(pos) and clicked == True and game_screen == "menu":
            game_screen = "level1"
            mixer.music.stop()  # Stop the menu music when switching to the game level
            soundtrack = "battle"  # Change to the new soundtrack for the level
            change_music(soundtrack)  # Load and play the new music      
            clicked = False

    elif game_screen == "info":
        draw_mainmenu()
        next_button.draw(screen)
        information()
        draw_movesList()
        if next_button.is_clicked(pos) and clicked == True:
            game_screen = "info2"
            clicked = False

    elif game_screen == "info2":
        draw_mainmenu()
        back_button.draw(screen)
        draw_demo()
        if back_button.is_clicked(pos) and clicked == True:
            game_screen = "menu"

    if game_screen == "level1":
        total_fighters = 3
        #draw background
        draw_lvl1()

        #draw panel
        draw_panel(1)

        #draw Mario
        mario.update()
        mario.draw()

        #draw Items


        #draw enemy
        for enemy in enemy_list_lvl1:
            enemy.update()
            enemy.draw()

        #draw the damage text
        damage_text_group.update()
        damage_text_group.draw(screen)

        #control player actions
        #reset action variables
        attack = False
        jump = False
        hammer = False
        fire = False
        spin = False
        mushroom = False
        syrup = False
        superMushroom = False
        
        #make sure mouse is visible
        # Ensure the mouse is visible initially
        pygame.mouse.set_visible(True)


        # Inside the game loop
        for count, enemy in enumerate(enemy_list_lvl1):
            if enemy.rect.collidepoint(pos) and enemy.alive and current_fighter == 1:
                # Hide mouse and change to fight icon
                pygame.mouse.set_visible(False)
                screen.blit(mouse_img, pos)
                if clicked and enemy.alive:
                    enemySelect()
                    target = enemy_list_lvl1[count]
                    clicked = False
                    
        draw_border()
        if target:  # If a target is selected, display its name
            targetName(target.name)
        else:
            targetName('')

        # Draw buttons and update UI
        drawUI()

        # Check for button clicks
        buttons = [jump_button, hammer_button, spin_button, fire_button, mush_button, syrup_button, super_mush_button]
        jump, hammer, spin, fire, mushroom, syrup, superMushroom = buttonClick(buttons, mario, enemy_list_lvl1, pos, clicked)

        # Player action
        if mario.alive:
                current_fighter, action_cooldown, target = marioAction(
                mario, target, current_fighter, action_cooldown, action_wait,
                jump, hammer, spin, fire, mushroom, syrup, superMushroom, damage_text_group, green
            )

        # Enemy action
        for count, enemy in enumerate(enemy_list_lvl1):
            if current_fighter == 2 + count:
                if enemy.alive and mario.alive:
                    action_cooldown += 1
                    if action_cooldown >= action_wait:
                        enemy.attack(mario)
                        current_fighter += 1
                        action_cooldown = 0
                else:
                    current_fighter += 1  # Skip dead enemies

        # If all fighters have had a turn, reset
        if current_fighter > total_fighters:
            current_fighter = 1
            target = None  # Reset target for the new round
            action_cooldown = 0

        # Check if all enemies are defeated
        if all(not enemy.alive for enemy in enemy_list_lvl1):
            allDead = True
            level2_button.draw(screen)
            #levelWin() loops need to fix
            if level2_button.is_clicked(pos) and clicked:
                game_screen = "level2"
                mixer.music.stop()  # Stop the menu music when switching to the game level
                soundtrack = "battle"  # Change to the new soundtrack for the level
                change_music(soundtrack)  # Load and play the new music      
                clicked = False
                mario.hp = 100
                mario.fp = 25
                mario.idle()
                win_animation_started = False
                win_animation_time = 0
                allDead = False

        # Check if Mario is defeated
        if not mario.alive:
            back_to_menu_button.draw(screen)
            retry_button.draw(screen)
            if retry_button.is_clicked(pos) and clicked:
                game_screen = "level1"
                clicked = False
                reset_level(enemy_list_lvl1)
                again()
            elif back_to_menu_button.is_clicked(pos) and clicked:
                game_screen = "menu"
                clicked = False
                reset_all_levels()
        winAnimation(enemy_list_lvl1)
        
    if game_screen == "level2":
        #draw background
        draw_lvl2()

        #draw panel
        draw_panel(2)

        #draw Mario
        mario.update()
        mario.draw()

        #draw Items


        #draw enemy
        for enemy in enemy_list_lvl2:
            enemy.update()
            enemy.draw()

        #draw the damage text
        damage_text_group.update()
        damage_text_group.draw(screen)

        #control player actions
        #reset action variables
        attack = False
        jump = False
        hammer = False
        fire = False
        spin = False
        mushroom = False
        syrup = False
        superMushroom = False

        #make sure mouse is visible
        # Ensure the mouse is visible initially
        pygame.mouse.set_visible(True)

        # Inside the game loop
        for count, enemy in enumerate(enemy_list_lvl2):
            if enemy.rect.collidepoint(pos) and enemy.alive:
                # Hide mouse and change to fight icon
                pygame.mouse.set_visible(False)
                screen.blit(mouse_img, pos)
                if clicked and enemy.alive:
                    enemySelect()
                    target = enemy_list_lvl2[count]
                    clicked = False
        
        draw_border()
        if target:  # If a target is selected, display its name
            targetName(target.name)
        else:
            targetName('')
        
        # Draw buttons and update UI
        drawUI()


        # Check for button clicks
        buttons = [jump_button, hammer_button, spin_button, fire_button, mush_button, syrup_button, super_mush_button]
        jump, hammer, spin, fire, mushroom, syrup, superMushroom = buttonClick(buttons, mario, enemy_list_lvl2, pos, clicked)

        # Player action
        if mario.alive:
            current_fighter, action_cooldown, target = marioAction(
                mario, target, current_fighter, action_cooldown, action_wait,
                jump, hammer, spin, fire, mushroom, syrup, superMushroom, damage_text_group, green
            )

        # Enemy action
        for count, enemy in enumerate(enemy_list_lvl2):
            if current_fighter == 2 + count:
                if enemy.alive and mario.alive:
                    action_cooldown += 1
                    if action_cooldown >= action_wait:
                        enemy.attack(mario)
                        current_fighter += 1
                        action_cooldown = 0
                else:
                    current_fighter += 1  # Skip dead enemies

        # If all fighters have had a turn, reset
        if current_fighter > total_fighters:
            current_fighter = 1
            target = None  # Reset target for the new round
            action_cooldown = 0

        # Check if all enemies are defeated
        if all(not enemy.alive for enemy in enemy_list_lvl2):
            level2_button.draw(screen)
            allDead = True
            if level2_button.is_clicked(pos) and clicked:
                game_screen = "level3"
                mixer.music.stop()  # Stop the menu music when switching to the game level
                soundtrack = "battle"  # Change to the new soundtrack for the level
                change_music(soundtrack)  # Load and play the new music      
                clicked = False
                mario.hp = 100
                mario.fp = 25
                mario.idle()
                win_animation_started = False
                win_animation_time = 0   
                allDead = False
   
        # Check if Mario is defeated
        if not mario.alive:
            back_to_menu_button.draw(screen)
            retry_button.draw(screen)
            if retry_button.is_clicked(pos) and clicked:
                game_screen = "level2"
                clicked = False
                reset_level(enemy_list_lvl2)
            elif back_to_menu_button.is_clicked(pos) and clicked:
                game_screen = "menu"
                clicked = False
                reset_all_levels()
        winAnimation(enemy_list_lvl2)
        
    if game_screen == "level3":
            #draw background
            draw_lvl3()

            #draw panel
            draw_panel(3)

            #draw Mario
            mario.update()
            mario.draw()

            #draw Items

            #draw enemy
            for enemy in enemy_list_lvl3:
                enemy.update()
                enemy.draw()

            #draw the damage text
            damage_text_group.update()
            damage_text_group.draw(screen)

            #control player actions
            #reset action variables
            attack = False
            jump = False
            hammer = False
            fire = False
            spin = False
            mushroom = False
            syrup = False
            superMushroom = False

            #make sure mouse is visible
            # Ensure the mouse is visible initially
            pygame.mouse.set_visible(True)

            # Inside the game loop
            for count, enemy in enumerate(enemy_list_lvl3):
                if enemy.rect.collidepoint(pos) and enemy.alive:
                    # Hide mouse and change to fight icon
                    pygame.mouse.set_visible(False)
                    screen.blit(mouse_img, pos)
                    if clicked and enemy.alive:
                        enemySelect()
                        target = enemy_list_lvl3[count]
                        clicked = False
        
            draw_border()
            if target:  # If a target is selected, display its name
                targetName(target.name)
            else:
                targetName('')
        

            # Draw buttons and update UI
            drawUI()

            # Check for button clicks
            buttons = [jump_button, hammer_button, spin_button, fire_button, mush_button, syrup_button, super_mush_button]
            jump, hammer, spin, fire, mushroom, syrup, superMushroom = buttonClick(buttons, mario, enemy_list_lvl3, pos, clicked)

            # Player action
            if mario.alive:
                current_fighter, action_cooldown, target = marioAction(
                mario, target, current_fighter, action_cooldown, action_wait,
                jump, hammer, spin, fire, mushroom, syrup, superMushroom, damage_text_group, green
            )
            
            # Enemy action
            for count, enemy in enumerate(enemy_list_lvl3):
                if current_fighter == 2 + count:
                    if enemy.alive and mario.alive:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if enemy.name == "Koopea" and enemy.alive:
                                if enemy.hp <= 15:
                                    healOrNoHeal = random.randrange(0,3)
                                    if healOrNoHeal == 0:
                                        heal_amount = min(20, enemy.max_hp - enemy.hp)     
                                        enemy.hp += heal_amount
                                        damage_text = DamageText(enemy.rect.centerx, enemy.rect.y+250, str(heal_amount), green)
                                        damage_text_group.add(damage_text)
                                        enemy.heal()
                                        current_fighter += 1
                                        action_cooldown = -40
                                    else:
                                        enemy.attack(mario)
                                        current_fighter += 1
                                        action_cooldown = -30
                                else:
                                    enemy.attack(mario)
                                    current_fighter += 1
                                    action_cooldown = -30
                            else: 
                                enemy.attack(mario)
                                current_fighter += 1
                                action_cooldown = 0
                    else:
                        current_fighter += 1  # Skip dead enemies

            # If all fighters have had a turn, reset
            if current_fighter > total_fighters:
                current_fighter = 1
                target = None  # Reset target for the new round
                action_cooldown = 0

            # Check if all enemies are defeated
            if all(not enemy.alive for enemy in enemy_list_lvl3):
                allDead = True
                level2_button.draw(screen)
                if level2_button.is_clicked(pos) and clicked:
                    game_screen = "level4"
                    mixer.music.stop()  # Stop the menu music when switching to the game level
                    soundtrack = "midBoss"  # Change to the new soundtrack for the level
                    change_music(soundtrack)  # Load and play the new music      
                    clicked = False
                    mario.hp = 100
                    mario.fp = 25
                    mario.idle()
                    win_animation_started = False
                    win_animation_time = 0
                    allDead = False
                                
            # Check if Mario is defeated
            if not mario.alive:
                back_to_menu_button.draw(screen)
                retry_button.draw(screen)
                if retry_button.is_clicked(pos) and clicked:
                    game_screen = "level3"
                    clicked = False
                    reset_level(enemy_list_lvl3)
                elif back_to_menu_button.is_clicked(pos) and clicked:
                    game_screen = "menu"
                    clicked = False
                    reset_all_levels()
            winAnimation(enemy_list_lvl3)       
    
    if game_screen == "level4":
        #draw background
        draw_lvl4()

        #draw panel
        draw_panel(4)
        total_fighters = 4

        #draw Mario
        mario.update()
        mario.draw()

        #draw Items

        #draw enemy
        for enemy in enemy_list_lvl4:
            enemy.update()
            enemy.draw()

        #draw the damage text
        damage_text_group.update()
        damage_text_group.draw(screen)

        #control player actions
        #reset action variables
        attack = False
        jump = False
        hammer = False
        fire = False
        spin = False
        mushroom = False
        syrup = False
        superMushroom = False

        #make sure mouse is visible
        # Ensure the mouse is visible initially
        pygame.mouse.set_visible(True)

        # Inside the game loop
        for count, enemy in enumerate(enemy_list_lvl4):
            if enemy.rect.collidepoint(pos) and enemy.alive:
                # Hide mouse and change to fight icon
                pygame.mouse.set_visible(False)
                screen.blit(mouse_img, pos)
                if clicked and enemy.alive:
                    enemySelect()
                    target = enemy_list_lvl4[count]
                    clicked = False
        
        draw_border()
        if target:  # If a target is selected, display its name
            targetName(target.name)
        else:
            targetName('')
        

        # Draw buttons and update UI
        drawUI()


        # Check for button clicks
        buttons = [jump_button, hammer_button, spin_button, fire_button, mush_button, syrup_button, super_mush_button]
        jump, hammer, spin, fire, mushroom, syrup, superMushroom = buttonClick(buttons, mario, enemy_list_lvl4, pos, clicked)

        # Player action
        if mario.alive:
                current_fighter, action_cooldown, target = marioAction(
                mario, target, current_fighter, action_cooldown, action_wait,
                jump, hammer, spin, fire, mushroom, syrup, superMushroom, damage_text_group, green
            )

        # Enemy action
        for count, enemy in enumerate(enemy_list_lvl4):
            if current_fighter == 2 + count:
                if enemy.alive and mario.alive:
                    action_cooldown += 1
                    if action_cooldown >= action_wait:
                        if enemy.name == "Koopea" and enemy.alive:
                            if enemy.hp <= 15:
                                healOrNoHeal = random.randrange(0,3)
                                if healOrNoHeal == 0:
                                    heal_amount = min(20, enemy.max_hp - enemy.hp)     
                                    enemy.hp += heal_amount
                                    damage_text = DamageText(enemy.rect.centerx, enemy.rect.y+250, str(heal_amount), green)
                                    damage_text_group.add(damage_text)
                                    enemy.heal()
                                    current_fighter += 1
                                    action_cooldown = -40
                                else:
                                    enemy.attack(mario)
                                    current_fighter += 1
                                    action_cooldown = -30
                            else:
                                enemy.attack(mario)
                                current_fighter += 1
                                action_cooldown = -30
                        else: 
                            enemy.attack(mario)
                            current_fighter += 1
                            action_cooldown = 0
                else:
                    current_fighter += 1  # Skip dead enemies

        # If all fighters have had a turn, reset
        if current_fighter > total_fighters:
            current_fighter = 1
            target = None  # Reset target for the new round
            action_cooldown = 0

        # Check if all enemies are defeated
        if all(not enemy.alive for enemy in enemy_list_lvl4):
            allDead = True
            level2_button.draw(screen)
            if level2_button.is_clicked(pos) and clicked:
                game_screen = "levelUP"
                mixer.music.stop()  # Stop the menu music when switching to the game level
                soundtrack = "levelUpOST"  # Change to the new soundtrack for the level
                change_music(soundtrack)  # Load and play the new music      
                clicked = False
                mario.hp = 100
                mario.fp = 25
                mario.idle()
                win_animation_started = False
                win_animation_time = 0
                allDead = False
                
        # Check if Mario is defeated
        if not mario.alive:
            back_to_menu_button.draw(screen)
            retry_button.draw(screen)
            if retry_button.is_clicked(pos) and clicked:
                game_screen = "level4"
                clicked = False
                reset_level(enemy_list_lvl4)
            elif back_to_menu_button.is_clicked(pos) and clicked:
                game_screen = "menu"
                clicked = False
                reset_all_levels()
        winAnimation(enemy_list_lvl4)  

    if game_screen == "levelUP":
        
        levelUP.update()
        levelUP.draw()        

        draw_text("As a bonus you get:", font, green, 68, 250)
        draw_text("3 mushrooms", font, green, 68, 280)
        draw_text("2 syrups", font, green, 68, 310)
        draw_text("3 strength points", font, green, 68, 340)


        next_button.draw(screen)
        if next_button.is_clicked(pos) and clicked:
            game_screen = "level5"
            mixer.music.stop()  # Stop the menu music when switching to the game level
            soundtrack = "boss"  # Change to the new soundtrack for the level
            change_music(soundtrack)  # Load and play the new music      
            clicked = False
            mario.hp = 100
            mario.fp = 25
            mario.mushrooms += 3
            mario.syrups += 2
            mario.strength += 5
            mario.idle()
            win_animation_started = False
            win_animation_time = 0

    if game_screen == "level5":
        #draw background
        draw_lvl5()

        #draw panel
        draw_panel(5)
        total_fighters = 2

        #draw Mario
        mario.update()
        mario.draw()

        #draw Items
        #itemAni.update()
        #itemAni.draw()

        #draw enemy
        for enemy in enemy_list_lvl5:
            enemy.update()
            enemy.draw()

        #draw the damage text
        damage_text_group.update()
        damage_text_group.draw(screen)

        #control player actions
        #reset action variables
        attack = False
        jump = False
        hammer = False
        fire = False
        spin = False
        mushroom = False
        syrup = False
        superMushroom = False

        #make sure mouse is visible
        # Ensure the mouse is visible initially
        pygame.mouse.set_visible(True)

        # Inside the game loop
        for count, enemy in enumerate(enemy_list_lvl5):
            if enemy.rect.collidepoint(pos) and enemy.alive:
                # Hide mouse and change to fight icon
                pygame.mouse.set_visible(False)
                screen.blit(mouse_img, pos)
                if clicked and enemy.alive:
                    enemySelect()
                    target = enemy_list_lvl5[count]
                    clicked = False
        
        draw_border()
        if target:  # If a target is selected, display its name
            targetName(target.name)
        else:
            targetName('')
        

        # Draw buttons and update UI
        drawUI()


        # Check for button clicks
        buttons = [jump_button, hammer_button, spin_button, fire_button, mush_button, syrup_button, super_mush_button]
        jump, hammer, spin, fire, mushroom, syrup, superMushroom = buttonClick(buttons, mario, enemy_list_lvl5, pos, clicked)

        # Player action
        if mario.alive:
                current_fighter, action_cooldown, target = marioAction(
                mario, target, current_fighter, action_cooldown, action_wait,
                jump, hammer, spin, fire, mushroom, syrup, superMushroom, damage_text_group, green
            )

        # Enemy action
        for count, enemy in enumerate(enemy_list_lvl5):
            if current_fighter == 2 + count:
                if enemy.alive and mario.alive:
                    action_cooldown += 1
                    groundOrFire = random.randrange(0,2)
                    if action_cooldown >= action_wait:
                        if enemy.hp <= 60:
                                healOrNoHeal = random.randrange(0,3)
                                if healOrNoHeal == 0:
                                    heal_amount = min(25, enemy.max_hp - enemy.hp)     
                                    enemy.hp += heal_amount
                                    damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(heal_amount), green)
                                    damage_text_group.add(damage_text)
                                    enemy.heal()
                                    current_fighter += 1
                                    action_cooldown = -40
                                else:
                                    if groundOrFire == 0:
                                        enemy.groundpound(mario)
                                        current_fighter += 1
                                        action_cooldown = -30
                                    elif groundOrFire == 1:
                                        enemy.firebreath(mario)
                                        current_fighter += 1
                                        action_cooldown = -30
                        else:
                            if groundOrFire == 0:
                                        enemy.groundpound(mario)
                                        current_fighter += 1
                                        action_cooldown = -30
                            elif groundOrFire == 1:
                                enemy.firebreath(mario)
                                current_fighter += 1
                                action_cooldown = -30
                else:
                    current_fighter += 1  # Skip dead enemies

        # If all fighters have had a turn, reset
        if current_fighter > total_fighters:
            current_fighter = 1
            target = None  # Reset target for the new round
            action_cooldown = 0

        # Check if all enemies are defeated
        if all(not enemy.alive for enemy in enemy_list_lvl5):
            allDead = True
            level2_button.draw(screen)
            if level2_button.is_clicked(pos) and clicked:
                game_screen = "levelUP2"
                mixer.music.stop()  # Stop the menu music when switching to the game level
                soundtrack = "levelUpOST"  # Change to the new soundtrack for the level
                change_music(soundtrack)  # Load and play the new music      
                clicked = False
                mario.hp = 100
                mario.fp = 25
                win_animation_started = False
                win_animation_time = 0
                allDead = False
                
        # Check if Mario is defeated
        if not mario.alive:
            back_to_menu_button.draw(screen)
            retry_button.draw(screen)
            if retry_button.is_clicked(pos) and clicked:
                game_screen = "level5"
                clicked = False
                reset_level(enemy_list_lvl5)
            elif back_to_menu_button.is_clicked(pos) and clicked:
                game_screen = "menu"
                clicked = False
                reset_all_levels()
        winAnimation(enemy_list_lvl5)  

    if game_screen == "levelUP2":
        
        levelUP.update()
        levelUP.draw()        

        draw_text("As a bonus you get:", font, green, 68, 250)
        draw_text("3 super mushrooms", font, green, 68, 280)
        draw_text("2 syrups", font, green, 68, 310)
        draw_text("50 HP", font, green, 68, 340)

        next_button.draw(screen)
        if next_button.is_clicked(pos) and clicked:
            game_screen = "level6"
            mixer.music.stop()  # Stop the menu music when switching to the game level
            soundtrack = "final"  # Change to the new soundtrack for the level
            change_music(soundtrack)  # Load and play the new music      
            clicked = False
            mario.max_hp = 130
            mario.hp = 150
            mario.fp = 30
            mario.superMushrooms += 3
            mario.strength += 5
            mario.idle()
            win_animation_started = False
            win_animation_time = 0


    if game_screen == "level6":
        #draw background
        draw_lvl6()

        #draw panel
        draw_panel(6)
        total_fighters = 2

        #draw Mario
        mario.update()
        mario.draw()

        #draw enemy
        for enemy in enemy_list_lvl6:
            enemy.update()
            enemy.draw()

        #draw the damage text
        damage_text_group.update()
        damage_text_group.draw(screen)

        #control player actions
        #reset action variables
        attack = False
        jump = False
        hammer = False
        fire = False
        spin = False
        mushroom = False
        syrup = False
        superMushroom = False


        #make sure mouse is visible
        # Ensure the mouse is visible initially
        pygame.mouse.set_visible(True)

        # Inside the game loop
        for count, enemy in enumerate(enemy_list_lvl6):
            if enemy.rect.collidepoint(pos) and enemy.alive:
                # Hide mouse and change to fight icon
                pygame.mouse.set_visible(False)
                screen.blit(mouse_img, pos)
                if clicked and enemy.alive:
                    enemySelect()
                    target = enemy_list_lvl6[count]
                    clicked = False
        
        draw_border()
        if target:  # If a target is selected, display its name
            targetName(target.name)
        else:
            targetName('')
        

        # Draw buttons and update UI
        drawUI()

        # Check for button clicks
        buttons = [jump_button, hammer_button, spin_button, fire_button, mush_button, syrup_button, super_mush_button]
        jump, hammer, spin, fire, mushroom, syrup, superMushroom = buttonClick(buttons, mario, enemy_list_lvl6, pos, clicked)

        # Player action
        if mario.alive:
                current_fighter, action_cooldown, target = marioAction(
                mario, target, current_fighter, action_cooldown, action_wait,
                jump, hammer, spin, fire, mushroom, syrup, superMushroom, damage_text_group, green
            )

        # Enemy action
        for count, enemy in enumerate(enemy_list_lvl6):
            if current_fighter == 2 + count:
                if enemy.alive and mario.alive:
                    action_cooldown += 1
                    spinPunchFire = random.randrange(0,3)
                    if action_cooldown >= action_wait:
                        if enemy.hp <= 115:
                                healOrNoHeal = random.randrange(0,4)
                                if healOrNoHeal == 0:
                                    heal_amount = min(30, enemy.max_hp - enemy.hp)     
                                    enemy.hp += heal_amount
                                    damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(heal_amount), green)
                                    damage_text_group.add(damage_text)
                                    enemy.heal()
                                    current_fighter += 1
                                    action_cooldown = -40
                                else:
                                    if spinPunchFire == 0:
                                        enemy.firebreath(mario)
                                        current_fighter += 1
                                        action_cooldown = -30
                                    elif spinPunchFire == 1:
                                        enemy.punch(mario)
                                        current_fighter += 1
                                        action_cooldown = -30
                                    elif spinPunchFire == 2:
                                        enemy.spin(mario)
                                        current_fighter += 1
                                        action_cooldown = -30
                        else:
                            if spinPunchFire == 0:
                                enemy.firebreath(mario)
                                current_fighter += 1
                                action_cooldown = -30
                            elif spinPunchFire == 1:
                                enemy.punch(mario)
                                current_fighter += 1
                                action_cooldown = -30
                            elif spinPunchFire == 2:
                                enemy.spin(mario)
                                current_fighter += 1
                                action_cooldown = -30
                else:
                    current_fighter += 1  # Skip dead enemies

        # If all fighters have had a turn, reset
        if current_fighter > total_fighters:
            current_fighter = 1
            target = None  # Reset target for the new round
            action_cooldown = 0

        # Check if all enemies are defeated
        if all(not enemy.alive for enemy in enemy_list_lvl6):
            allDead = True
            level2_button.draw(screen)
            if level2_button.is_clicked(pos) and clicked:
                game_screen = "menu"
                mixer.music.stop()  # Stop the menu music when switching to the game level
                soundtrack = "wonderTitleScreen"  # Change to the new soundtrack for the level
                change_music(soundtrack)  # Load and play the new music      
                clicked = False
                mario.hp = 100
                mario.fp = 25
                win_animation_started = False
                win_animation_time = 0
                allDead = False
                reset_all_levels()
                
        # Check if Mario is defeated
        # Check if Mario is defeated
        if not mario.alive:
            back_to_menu_button.draw(screen)
            retry_button.draw(screen)
            if retry_button.is_clicked(pos) and clicked:
                game_screen = "level6"
                clicked = False
                reset_level(enemy_list_lvl6)
            elif back_to_menu_button.is_clicked(pos) and clicked:
                game_screen = "menu"
                clicked = False
                reset_all_levels()
        winAnimation(enemy_list_lvl6)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()

pygame.quit()