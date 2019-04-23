import pygame, sys
#from pygame.locals import *
import itertools
from pygame.sprite import Sprite

#class Game():
    # def __init__():
    #     pygame.init()


def game():
    pygame.init()
    img = pygame.image.load("blorenge.png")
    pygame.display.set_icon(img) #sets an icon for the window

    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

    running = True
  
    while running:
        screen.blit(img, (0,0)) #replace img with an image the size
                                #of the screen to serve as background
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update() 

game()