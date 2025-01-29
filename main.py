import pygame
import random
import sys

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((700, 650))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION = random.randint(30, 620)
Y_POSITION = 600
jumping = False

Y_GRAVITY = 0.35
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("images/apple.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/banana.png"), (48, 64))
BACKGROUND = pygame.image.load("images/backgroung.png")

FRUITS_RECT = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    SCREEN.blit(BACKGROUND, (0, 0))
    
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        FRUITS_RECT = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, FRUITS_RECT)

        
    else:
        FRUITS_RECT = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, FRUITS_RECT)
        X_POSITION = random.randint(30, 620)

        
        

    pygame.display.update()
    CLOCK.tick(60)