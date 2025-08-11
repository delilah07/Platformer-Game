import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init() # initialize pygame

pygame.display.set_caption('Platformer') # set the current window caption

WIDTH, HEIGHT = 1000, 800 
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT)) # create window

def get_bg(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect() # give x, y, width and height
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    
    return tiles, image

def draw(window, bg, bg_img):
    for tile in bg:
        window.blit(bg_img, tile) #draw one image onto another

    pygame.display.update() #Update portions of the screen for software displays

def main(window):
    clock = pygame.time.Clock() #create an object to help track time

    run = True
    while run:
        clock.tick(FPS) # run 60 frames per second
        bg, bg_image = get_bg("Blue.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, bg, bg_image)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)