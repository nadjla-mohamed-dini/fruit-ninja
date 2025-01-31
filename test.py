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
y = random.randint(100, 400)

# Fruit size
FRUIT_SIZE_X = random.randint(30, 100)
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



FRUITS_RECT = fruit_image.get_rect(center=(x, y))



running = True

while running:
    CLOCK.tick(120)
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(letter_image, (0, 0))



    FRUITS_RECT = center=(x, y)
    SCREEN.blit(fruit_image, FRUITS_RECT)
    SCREEN.blit(letter_image, FRUITS_RECT)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        print('detected')


    pygame.display.flip()

pygame.quit()