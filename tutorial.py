import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init() # initialize pygame

pygame.display.set_caption('Platformer') # set the current window caption

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800 
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT)) # create window

def main(window):
    clock = pygame.time.Clock() #create an object to help track time

    run = True
    while run:
        clock.tick(FPS) # run 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)