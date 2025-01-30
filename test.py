import pygame
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("fruits ninja")
WHITE = (255, 255, 255)
BACKGROUND = pygame.image.load("images/background.png")

FRUIT_RECT = pygame.Rect(250,250,100,100)

BANANA = pygame.image.load("images/fruits/banana.png")
AA = pygame.image.load("images/letters/a_letter.png")





running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    SCREEN.blit(BANANA, AA)

pygame.quit()