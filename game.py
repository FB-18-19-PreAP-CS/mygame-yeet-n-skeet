import pygame
import os, sys
#from pygame.locals import *
import itertools
#from pygame.sprite import Sprite


class Yeet(pygame.sprite.Sprite):
    def __init__(self, color = (0,0,0), width = 100, hieght = 100):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("yeet.jpg")

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Game():
    def __init__(self):
        pygame.init()
        img = pygame.image.load("blorenge.png")
        #yee = pygame.image.load("yeet.jpg")
        pygame.display.set_icon(img) #sets an icon for the window

        screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

        player_1 = Yeet()


        running = True
        while running:
            screen.blit(img, (0,0)) #replace img with an image the size
                                    #of the screen to serve as background
            y.set_pos(0,0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #pygame.display.update() 
Game()
