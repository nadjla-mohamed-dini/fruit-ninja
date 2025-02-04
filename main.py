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



# X axis
x = random.randint(30, 630)
# Y axis
y = 550

# Fruit size
FRUIT_SIZE_X = random.randint(50, 100)
FRUIT_SIZE_Y = FRUIT_SIZE_X
 

# Choice fruit
def fruit():
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
letter_image = pygame.image.load("images/letters/e_letter.png")
def letter():
    random_letter = random.randint(1, 3)
    if random_letter == 1:
        letter_image = pygame.image.load("images/letters/a_letter.png")
    if random_letter == 2:
        letter_image = pygame.image.load("images/letters/z_letter.png")
    if random_letter == 3:
        letter_image = pygame.image.load("images/letters/e_letter.png")


# Fruit definition
fruit_image = pygame.image.load("images/letters/a_letter.png")
FRUITS_RECT = fruit_image.get_rect(center=(x, y))

def spawn_fruit():
    fruit()
    letter()
    FRUITS_RECT = center=(x, y)
    SCREEN.blit(fruit_image, FRUITS_RECT)
    SCREEN.blit(letter_image, FRUITS_RECT)  




running = True

while running:
    CLOCK.tick(120)
    SCREEN.blit(BACKGROUND, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    spawn_fruit()


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
            jumping = True
    if keys_pressed[pygame.K_z] and Y_POSITION < 650:
        fruit()
        letter()

    if Y_POSITION > 660:
        print("falling")





    pygame.display.flip()

pygame.quit()