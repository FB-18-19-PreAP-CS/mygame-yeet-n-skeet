import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite

#class Game():
    # def __init__():
    #     pygame.init()

class Game():
    def __init__(self):
        pygame.init()
        img = pygame.image.load("blorenge.png")
        pygame.display.set_icon(img) #sets an icon for the window

        screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

        running = True
    
        img = pygame.image.load('')
        while running:
            screen.blit(img, (0,0)) #replace img with an image the size
                                    #of the screen to serve as background
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update() 

game()


# class yeet(Sprite):

#    def __init__(self, screen, img_filename, init_pos, init_dir, speed):
#        Sprite.__init__(self)

#        self.image = pygame.Surface([width, height])
#        self.image.fill(color)

#        self.rect = self.image.get_rect()
#        self.char_img = pygame.image.load("Copy of yeet.jpg")
#        self.image = self.char_img
