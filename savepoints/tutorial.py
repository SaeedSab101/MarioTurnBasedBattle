import pygame
import random
import tkinter as tk

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
total_fighters = 2
action_cooldown = 0
action_wait = 90
attack = False
mushroom = False
mushroom_effect = 15
clicked = False

#define fonts
font = pygame.font.SysFont('Times New Roman', 26)

#define colours
red = (255, 0, 0)
green = (0, 255, 0)

#load images
#background images
background_img = pygame.image.load('images/MLSSbeanbean.gif').convert_alpha()
scaled_image = pygame.transform.scale(background_img, (screen_width, screen_height - bottom_panel))
#panel image
panel_img = pygame.image.load('images/Panel.png').convert_alpha()
#mouse image
mouse_img = pygame.image.load('images/hammer.png').convert_alpha()

#create function for drawing text
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))
#function for drawing background
def draw_bg():
    screen.blit(scaled_image, (0,0))

#function for drawing panel
def draw_panel():
    #draw panel
    screen.blit(panel_img, (0,600))
    #show mario stats
    draw_text(f'{mario.name} HP: {mario.hp}', font, red, 100, 600)

    #loop if multiple enemies
    for count, enemy in enumerate(enemy_list):
        #show name and health
        draw_text(f'{enemy.name} HP: {enemy.hp}', font, red, 600, (600) + count * 60)

#Mario Class
class Mario():
    def __init__(self, x, y, name, max_hp, strength, mushrooms):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_mushrooms = mushrooms
        self.mushrooms = mushrooms
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        
        #load images for idle
        temp_list = []
        for i in range (8):
            image = pygame.image.load(f'images/{self.name}/Idle/{i}.png')
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for attack
        temp_list = []
        for i in range (11):
            image = pygame.image.load(f'images/{self.name}/Hammer/{i}.png')
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        animation_cooldown = 120
        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()

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

    def draw(self):
        screen.blit(self.image, self.rect)


#Enemy class
class Enemy():
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
        
        #load images for idle
        temp_list = []
        for i in range (40):
            image = pygame.image.load(f'images/Enemy/Idle/{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load images for attack
        temp_list = []
        for i in range (35):
            image = pygame.image.load(f'images/Enemy/Punch/{i}.png')
            image = pygame.transform.scale(image, (image.get_width() * 2.5, image.get_height() * 2.5))
            temp_list.append(image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        animation_cooldown = 50
        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
           self.idle()

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
        
    def draw(self):
        screen.blit(self.image, self.rect)

class HealthBar():
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

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
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


mario = Mario(450, 400, 'Mario', 100, 10, 3)
enemy = Enemy(750, 375, 'Enemy', 150, 20)

enemy_list = []
enemy_list.append(enemy)

mario_health_bar = HealthBar(100, 700, mario.hp, mario.max_hp)
enemy_health_bar = HealthBar(500, 700, enemy.hp, enemy.max_hp)

# Button settings
jump_button_img = pygame.image.load('images/Buttons/jumpButton.png')  # Load button image
jump_button_rect = jump_button_img.get_rect()
jump_button_rect.topleft = (200, 600)  # Set the button position

hammer_button_img = pygame.image.load('images/Buttons/hammerButton.png')  # Load button image
hammer_button_rect = hammer_button_img.get_rect()
hammer_button_rect.topleft = (300, 600)  # Set the button position

spin_button_img = pygame.image.load('images/Buttons/spinButton.png')  # Load button image
spin_button_rect = spin_button_img.get_rect()
spin_button_rect.topleft = (200, 700)  # Set the button position

fire_button_img = pygame.image.load('images/Buttons/fireButton.png')  # Load button image
fire_button_rect = fire_button_img.get_rect()
fire_button_rect.topleft = (300, 700)  # Set the button position

mush_button_img = pygame.image.load('images/Buttons/mushroomButton.png')  # Load button image
mush_button_rect = mush_button_img.get_rect()
mush_button_rect.topleft = (400, 650)  # Set the button position


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
jump_button = Button(jump_button_img, 200, 600)
hammer_button = Button(hammer_button_img, 300, 600)
spin_button = Button(spin_button_img, 200, 700)
fire_button = Button(fire_button_img, 300, 700)
mush_button = Button(mush_button_img, 400, 650)



run = True
while run:
    
    clock.tick(fps)

    #draw background
    draw_bg()

    #draw panel
    draw_panel()

    #draw health bars
    mario_health_bar.draw(mario.hp)
    enemy_health_bar.draw(enemy.hp)

    #draw Mario
    mario.update()
    mario.draw()

    #draw enemy
    for enemy in enemy_list:
        enemy.update()
        enemy.draw()

    #draw the damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    #control player actions
    #reset action variables
    attack = False
    mushroom = False
    target = None

    #make sure mouse is visible
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, enemy in enumerate(enemy_list):
        if enemy.rect.collidepoint(pos):
            #hide mouse
            pygame.mouse.set_visible(False)
            #change mouse to fight icon
            screen.blit(mouse_img, pos)
            if clicked == True:
                attack = True
                target = enemy_list[count]
 
    # Inside the game loop
    jump_button.draw(screen)
    hammer_button.draw(screen)
    spin_button.draw(screen)
    fire_button.draw(screen)
    mush_button.draw(screen)
    draw_text(str(mario.mushrooms), font, red, 475, 675)

    # Check for button clicks
    for button in [jump_button, hammer_button, spin_button, fire_button, mush_button]:
        if button.is_clicked(pos) and clicked:
            # Handle button click actions
            if button == jump_button:
                print("Jump button clicked")
            elif button == hammer_button:
                print("Hammer button clicked")
            elif button == spin_button:
                print("Spin button clicked")
            elif button == fire_button:
                print("Fire button clicked")
            elif button == mush_button:
                mushroom = True



    #player action
    if mario.alive == True:
        if current_fighter == 1:
            action_cooldown +=1
            if action_cooldown >= action_wait:
                #look for player action
                #attack
                if attack == True and target != None:
                    mario.attack(target)
                    current_fighter += 1
                    action_cooldown = 0
                #mushroom
                if mushroom == True:
                    if mario.mushrooms > 0:
                        #check if mushroom heals beyond max health
                        if mario.max_hp - mario.hp > mushroom_effect:
                            heal_amount = mushroom_effect
                            mario.hp += heal_amount
                        else:
                            heal_amount = mario.max_hp - mario.hp
                        mario.hp += heal_amount
                        mario.mushrooms -= 1
                        damage_text = DamageText(mario.rect.centerx, mario.rect.y, str(heal_amount), green)
                        damage_text_group.add(damage_text)
                        current_fighter += 1
                        action_cooldown = 0
                        
    #enemy action
    for count, enemy in enumerate(enemy_list):
        if current_fighter == 2 + count:
            if enemy.alive == True:
                action_cooldown +=1
                if action_cooldown >= action_wait:
                    #look for player action
                    #attack
                    enemy.attack(mario)
                    current_fighter += 1
                    action_cooldown = 0
            else:
                current_fighter +=1

    #if all fighters have had a turn then reset
    if current_fighter > total_fighters:
        current_fighter = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()

pygame.quit()