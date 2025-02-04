

import pygame
import time
import random
import sys


pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("fruits ninja")
BACKGROUND = pygame.image.load("images/background.png")


X_POSITION = random.randint(30, 620)
Y_POSITION = 880
jumping = False
Y_GRAVITY = 1
JUMP_HEIGHT = 40
Y_VELOCITY = JUMP_HEIGHT



CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("fruits ninja")
WHITE = (255, 255, 255)
BACKGROUND = pygame.image.load("images/background.png")

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("images/fruits/banana.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/fruits/banana.png"), (48, 64))
AA = pygame.image.load("images/letters/a_letter.png")
ZZ = pygame.image.load("images/letters/z_letter.png")
EE = pygame.image.load("images/letters/e_letter.png")


banana_image = pygame.image.load("images/letters/a_letter.png")
FRUITS_RECT = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))



running = True

while running:
    CLOCK.tick(120)
    SCREEN.blit(BACKGROUND, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    
    
    random_letter = random.randint(1, 3)
    if random_letter == 1:
                banana_image = pygame.image.load("images/letters/a_letter.png")
    if random_letter == 2:
                banana_image = pygame.image.load("images/letters/z_letter.png")
    if random_letter == 3:
                banana_image = pygame.image.load("images/letters/e_letter.png")

    SCREEN.blit(banana_image, (0, 0))


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
            jumping = True
    if keys_pressed[pygame.K_z] and Y_POSITION < 650:
        JUMPING_SURFACE = pygame.image.load("images/blank_fruit.png")

    if Y_POSITION > 660:
           JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/fruits/banana.png"), (48, 64))


    if jumping:
        Y_POSITION -= Y_VELOCITY 
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            JUMP_HEIGHT = 40
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        FRUITS_RECT = center=(X_POSITION, Y_POSITION)
        SCREEN.blit(JUMPING_SURFACE, FRUITS_RECT)
        SCREEN.blit(banana_image, FRUITS_RECT)

        
    else:
        FRUITS_RECT =center=(X_POSITION, Y_POSITION)
        SCREEN.blit(STANDING_SURFACE, FRUITS_RECT)
        SCREEN.blit(banana_image, FRUITS_RECT)
        X_POSITION = random.randint(30, 635)


    pygame.display.flip()

pygame.quit()