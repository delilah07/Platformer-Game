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

class Player(pygame.sprite.Sprite): # the base class for visible game objects
    COLOR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)

def draw(window, bg, bg_img, player):
    for tile in bg:
        window.blit(bg_img, tile) #draw one image onto another

    player.draw(window)

    pygame.display.update() #Update portions of the screen for software displays

def main(window):
    clock = pygame.time.Clock() #create an object to help track time
    bg, bg_image = get_bg("Blue.png")
    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS) # run 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, bg, bg_image, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)