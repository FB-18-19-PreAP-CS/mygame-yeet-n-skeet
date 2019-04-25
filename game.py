import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite

# class Avatar(pygame.sprite.Sprite):
#     def __init__(self, width, height):
#         pygame.sprite.Sprite.__init__(self)

#         self.image = pygame.Surface([width, height])
#         self.image.fill('white')
#         self.rect = self.image.get_rect()

class Yeet(pygame.sprite.Sprite):
    def __init__(self, color = (0,0,0), width = 100, hieght = 100):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("yeet.png")

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Game():
    def __init__(self):
        pygame.init()
        self.Avatar = pygame.image.load("yeet.png")
        self.img = pygame.image.load("blorenge.png")
        pygame.display.set_icon(self.img) #sets an icon for the window
        self.player = Yeet()
        self.all_sprites = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Yeet 'n' Skeet") #name for the window
        
        running = True
    
        
        while running:
            
            #self.screen.blit(self.Avatar, (500,500)) #replace img with an image the size
                                    #of the screen to serve as background
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update() 

Game()