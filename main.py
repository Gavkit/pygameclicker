import pygame
from sys import exit
from function import *

pygame.init()
init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            coins = coins + 1

    DrawText(f"Coin Amount: {coins}", 'black', 'white', 30, 15, 20, 1)
    update()
