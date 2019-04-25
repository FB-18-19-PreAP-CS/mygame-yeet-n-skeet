import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite

#class Game():
    # def __init__():
    #     pygame.init()
# class Avatar(pygame.sprite.Sprite):
#     def __init__(self, width, height):
#         pygame.sprite.Sprite.__init__(self)

#         self.image = pygame.Surface([width, height])
#         self.image.fill('white')
#         self.rect = self.image.get_rect()
class Game():
    def __init__(self):
        pygame.init()
        self.Avatar1 = pygame.image.load("yeet.png")
        self.Skeet = pygame.image.load("skeet.png")
        self.img = pygame.image.load("blorenge.png")
        pygame.display.set_icon(self.img) #sets an icon for the window

        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

        
        
        
        running = True
    
        
        while running:
            self.screen.blit(self.img, (500,500)) #replace img with an image the size
                                    #of the screen to serve as background
            self.screen.blit(self.Avatar1, (50, 870))
            self.screen.blit(self.Skeet, (870, 870))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update() 

Game()

# blit(avatar(x,y))


# class yeet(Sprite):

#    def __init__(self, screen, img_filename, init_pos, init_dir, speed):
#        Sprite.__init__(self)

#        self.image = pygame.Surface([width, height])
#        self.image.fill(color)

#        self.rect = self.image.get_rect()
#        self.char_img = pygame.image.load("Copy of yeet.jpg")
#        self.image = self.char_img
