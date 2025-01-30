import pygame
import random
import sys
import os

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((700, 650))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION = random.randint(30, 620)
Y_POSITION = 880
jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 40
Y_VELOCITY = JUMP_HEIGHT
AA = pygame.image.load("images/letters/a_letter.png")
ZZ = pygame.image.load("images/letters/z_letter.png")
EE = pygame.image.load("images/letters/e_letter.png")

BACKGROUND = pygame.image.load("images/background.png")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)






STANDING_SURFACE = pygame.transform.scale(pygame.image.load("images/fruits/apple.png"), (48, 64))
LETTER = pygame.transform.scale(ZZ, (20, 30))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/fruits/apple.png"), (48, 64))
BACKGROUND = pygame.image.load("images/background.png")

FRUITS_RECT = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))


COLLISION = pygame.transform.scale(pygame.image.load("images/collision.png"), (700, 650))



RUNNING = True



def random_file(directory):
    files = os.listdir(directory)
    random_file = random.choice(files)
    return random_file
directory = 'images/letters'
selected_file = random_file(directory)
print("Selected file:", selected_file)


# Game loop
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(COLLISION, (0, 0))



    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True
       

# Moving fruits
    if jumping:
        Y_POSITION -= Y_VELOCITY 
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            JUMP_HEIGHT = 40

            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        FRUITS_RECT = center=(X_POSITION, Y_POSITION)
        SCREEN.blit(JUMPING_SURFACE, FRUITS_RECT)
        SCREEN.blit(LETTER, FRUITS_RECT)


        
    else:
        FRUITS_RECT =center=(X_POSITION, Y_POSITION)
        SCREEN.blit(STANDING_SURFACE, FRUITS_RECT)
        SCREEN.blit(LETTER, FRUITS_RECT)

        X_POSITION = random.randint(30, 635)

        


    pygame.display.update()
    CLOCK.tick(30)


    # faire des fond differents accordés avec la musique, modifiable dans les paramètres