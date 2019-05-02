import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite
import time

# class Avatar(pygame.sprite.Sprite):
#     def __init__(self, width, height):
#         pygame.sprite.Sprite.__init__(self)

#         self.image = pygame.Surface([width, height])
#         self.image.fill('white')
#         self.rect = self.image.get_rect()


# def move_left(x,y):
#     x -= 100
#     return x

class Game():
    def __init__(self):
        pygame.init()
        self.yeet = pygame.image.load("yeet.png")
        #self.yeet.set_colorkey((255,255,255))
        #self.yeet_pos = (x,y) 

        self.skeet = pygame.image.load("skeet.png")
        #self.skeet.set_colorkey((255,255,255))
        #self.skeet_pos = (870, 870)

        self.img = pygame.image.load("blorenge.png")
        pygame.display.set_icon(self.img) #sets an icon for the window

        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Yeet 'n' Skeet") #name for the window
        
        self.screen.blit(self.yeet, (500,500))

        self.running = True

    # def yeet_left(self):  #will change to cover both later. trying Yeet first
    #     yeet_pos = self.yeet.get_rect()
    #     self.screen.blit(self.yeet, (yeet_pos[0]-50, yeet_pos[1]))

    # def yeet_right(self):
    #     yeet_pos = self.yeet.get_rect()
    #     self.screen.blit(self.yeet, (yeet_pos[0]+50, yeet_pos[1]))

    # def yeet_jump(self):
    #     yeet_pos = self.yeet.get_rect()
    #     self.screen.blit(self.yeet, (yeet_pos[0], yeet_pos[1]-50))
    #     self.screen.blit(self.yeet, (yeet_pos[0], yeet_pos[1]+50))
        

    def start(self):
        yeet_x = 50
        yeet_y = 870
        move_x = 7 #speed of how many pixels it moves
        move_y = 7
        self.screen.blit(self.yeet, (yeet_x,yeet_y))
        while self.running:
            #self.screen.blit(self.img,(500,500)) #replace img with an image the size
                                    #of the screen to serve as background

            #self.yeet_left()
            
            #
            # self.screen.blit(self.yeet, (50, 870))

            #self.screen.blit(self.skeet, (870, 870))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]: # move right
                yeet_x += move_x
            if keys[pygame.K_LEFT]: # move left
                yeet_x -= move_x
            if keys[pygame.K_UP]: # jump
                yeet_y -= move_y
                self.yeet.time.wait(100000)
                yeet_y += move_y
                        
            self.screen.fill((0,0,0))
            self.screen.blit(self.img,(500,500))
            self.screen.blit(self.yeet, (yeet_x,yeet_y))
            pygame.display.update()


def main():
    g = Game()
    #g.yeet_left()
    g.start()

if __name__ == "__main__":
    main()



# class Yeet(pygame.sprite.Sprite):
#     def __init__(self, color = (0,0,0), width = 100, hieght = 100):
#         pygame.sprite.Sprite.__init__(self)

#         self.image = pygame.image.load("yeet.png")

#         self.rect = self.image.get_rect()

#     def set_pos(self, x, y):
#         self.rect.x = x
#         self.rect.y = y

# class Game():
#     def __init__(self):
#         pygame.init()
#         self.Avatar = pygame.image.load("yeet.png")
#         self.img = pygame.image.load("blorenge.png")
#         pygame.display.set_icon(self.img) #sets an icon for the window
#         self.player = Yeet()
#         self.all_sprites = pygame.sprite.Group()

#         self.screen = pygame.display.set_mode((1000,1000))
#         pygame.display.set_caption("Yeet 'n' Skeet") #name for the window
        
#         running = True
    
        
#         while running:
#             self.screen.blit(self.all_sprites)
#             #self.screen.blit(self.Avatar, (500,500)) #replace img with an image the size
#                                     #of the screen to serve as background
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False

#             pygame.display.update() 

# Game()

#https://dr0id.bitbucket.io/legacy/pygame_tutorial01.html