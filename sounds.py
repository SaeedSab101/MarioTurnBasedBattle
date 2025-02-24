import random
import pygame
from pygame import mixer
mixer.init()

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