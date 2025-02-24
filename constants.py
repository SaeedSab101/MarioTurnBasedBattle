import pygame
import pyglet

pygame.init()

#import custom font
fontName = "fonts/SuperMario256.ttf"
fontTarget = "fonts/speechText.ttf"
pyglet.font.add_file(f'{fontName}')
pyglet.font.add_file(f'{fontTarget}')

#define fonts
font = pygame.font.Font(fontName, 26)
titleFont = pygame.font.Font(fontName, 40)
font2 = pygame.font.Font(fontTarget, 45)


#define colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 139)
