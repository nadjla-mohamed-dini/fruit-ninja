def fruit():
    FRUITS_RECT = center=(x, y)
    SCREEN.blit(fruit_image, FRUITS_RECT)
    SCREEN.blit(letter_image, FRUITS_RECT)   
    time.sleep(1)

class Fruit:
    def __init__(self,x,y,FRUIT_SIZE_X, FRUIT_SIZE_Y, fruit_image, letter_image):
        self.x = x
        self.y = y
        self.FRUIT_SIZE_X = FRUIT_SIZE_X
        self.FRUIT_SIZE_Y = FRUIT_SIZE_Y
        self.fruit_image = fruit_image
        self.letter_image = letter_image

class Fruit2:
    def __init__(self):
        self.x = x
        self.y = y
        self.FRUIT_SIZE_X = FRUIT_SIZE_X
        self.FRUIT_SIZE_Y = FRUIT_SIZE_Y
        self.fruit_image = fruit_image
        self.letter_image = letter_image


#class Fruit:
def __init__(self,x,y,FRUIT_SIZE_X, FRUIT_SIZE_Y, fruit_image, letter_image):
        self.x = x
        self.y = y
        self.FRUIT_SIZE_X = FRUIT_SIZE_X
        self.FRUIT_SIZE_Y = FRUIT_SIZE_Y
        self.fruit_image = fruit_image
        self.letter_image = letter_image




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




import pygame
import time
import random
import sys
import os
pygame.init()


CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((700, 650))
pygame.display.set_caption("Fruits ninja")
WHITE = (255, 255, 255)
BACKGROUND = pygame.image.load("images/background.png")




# X axis
x = random.randint(30, 630)
# Y axis
y = 550

# Fruit size
FRUIT_SIZE_X = random.randint(50, 100)
FRUIT_SIZE_Y = FRUIT_SIZE_X

# Choice fruit
BANANA = pygame.transform.scale(pygame.image.load("images/fruits/banana.png"), (FRUIT_SIZE_X, FRUIT_SIZE_Y))
APPLE = pygame.transform.scale(pygame.image.load("images/fruits/apple.png"), (FRUIT_SIZE_X, FRUIT_SIZE_Y))
GRAPE = pygame.transform.scale(pygame.image.load("images/fruits/grape.png"), (FRUIT_SIZE_X, FRUIT_SIZE_Y))
STRAWBERRY = pygame.transform.scale(pygame.image.load("images/fruits/strawberry.png"), (FRUIT_SIZE_X, FRUIT_SIZE_Y))
BOMB = pygame.transform.scale(pygame.image.load("images/fruits/bomb.png"), (FRUIT_SIZE_X, FRUIT_SIZE_Y))
ICE = pygame.transform.scale(pygame.image.load("images/fruits/ice.png"), (FRUIT_SIZE_X, FRUIT_SIZE_Y))


random_fruit = random.randint(1, 6)
if random_fruit == 1:
    fruit_image = APPLE
if random_fruit == 2:
    fruit_image = GRAPE
if random_fruit == 3:
    fruit_image = BANANA
if random_fruit == 4:
    fruit_image = STRAWBERRY
if random_fruit == 5:
    fruit_image = ICE
if random_fruit == 6:
    fruit_image = BOMB



# Choice letter

random_letter = random.randint(1, 3)
if random_letter == 1:
    letter_image = pygame.image.load("images/letters/a_letter.png")
if random_letter == 2:
    letter_image = pygame.image.load("images/letters/z_letter.png")
if random_letter == 3:
    letter_image = pygame.image.load("images/letters/e_letter.png")


# Fruit definition
FRUITS_RECT = fruit_image.get_rect(center=(x, y))







running = True

while running:
    print("e")
    # Some definitions for the loop
    CLOCK.tick(120)
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(letter_image, (0, 0))



    FRUITS_RECT = center=(x, y)
    SCREEN.blit(fruit_image, FRUITS_RECT)
    SCREEN.blit(letter_image, FRUITS_RECT)    




    # Quit function 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        jump = True
        print('detected')

    pygame.display.flip()

pygame.quit()



import pygame
import time
import random
import sys


pygame.init()

X_POSITION = random.randint(30, 620)
Y_POSITION = 880
jumping = False
Y_GRAVITY = 1
JUMP_HEIGHT = 40
Y_VELOCITY = JUMP_HEIGHT


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650

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