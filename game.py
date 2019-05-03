import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite
from random import randint

num = randint(1,2)



num = 1

if num == 1:
    pygame.init()
    yeet = pygame.image.load("yeet transparent.png")
    Skeet = pygame.image.load("skeet transparent.png")
    Dave = pygame.image.load('Dave transparent.png')
    img = pygame.image.load("level 1 wip.png")
    pygame.display.set_icon(img) #sets an icon for the window

    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Yeet 'n' Skeet") #name for the window
    yeet_x = 10
    yeet_y = 905
    move = 5
    Skeet_x =879
    Skeet_y =905   
            
            
    running = True
        
            
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        
        #temp yeet controls
        if keys[pygame.K_DOWN]:
            yeet_y += move
        if keys[pygame.K_UP]:
            yeet_y -= move
        
        
        if keys[pygame.K_RIGHT]:
            yeet_x +=move
        if keys[pygame.K_LEFT]:
            yeet_x -= move
        if keys[pygame.K_a]:
            Skeet_x -= move
        if keys[pygame.K_d]:
            Skeet_x += move
            
        if yeet_x <= 0:
            yeet_x += move
        if Skeet_x <= 0:
            Skeet_x += move
        if yeet_y >= 930:
            yeet_y -= move
        if Skeet_y >= 930:
            Skeet_y -= move
        
        screen.blit(img, (1,1))
        screen.blit(Dave, (450,10))
        screen.blit(yeet, (yeet_x,yeet_y))
        screen.blit(Skeet, (Skeet_x,Skeet_y))
        pygame.display.update()


elif num == 2:
    pygame.init()
    yeet = pygame.image.load("yeet transparent.png")
    Skeet = pygame.image.load("skeet transparent.png")
    Dave = pygame.image.load('Dave transparent.png')
    img = pygame.image.load("blorenge.png")
    pygame.display.set_icon(img) #sets an icon for the window

    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

    yeet_x = 10
    yeet_y = 905
    move = 5
    Skeet_x =879
    Skeet_y =905   
        
        
    running = True
    
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        
        #temp yeet controls
        if keys[pygame.K_DOWN]:
            yeet_y += move
        if keys[pygame.K_UP]:
            yeet_y -= move
        if keys[pygame.K_w]:
            Skeet_y += move
        if keys[pygame.K_s]:
            Skeet_y -= move
        
        if keys[pygame.K_RIGHT]:
            yeet_x +=move
        if keys[pygame.K_LEFT]:
            yeet_x -= move
        if keys[pygame.K_a]:
            Skeet_x -= move
        if keys[pygame.K_d]:
            Skeet_x += move
            

        #boundaries
        if yeet_x <= -10:
            yeet_x += move
        if Skeet_x <= -10:
            Skeet_x += move
        if yeet_x >= 930:
            yeet_x -= move
        if Skeet_x >= 930:
            Skeet_x -= move
        if yeet_y <= 0:
            yeet_y -= move
        if yeet_y >= 900:
            yeet_y -= move
        if Skeet_y <= 0:
            Skeet_y += move
        if Skeet_y >= 900:
            Skeet_y -= move
        
        screen.blit(img, (1,1))
        screen.blit(Dave, (50,10))
        screen.blit(yeet, (yeet_x,yeet_y))
        screen.blit(Skeet, (Skeet_x,Skeet_y))
        pygame.display.update()



# pygame.init()
# yeet = pygame.image.load("yeet.png")
# Skeet = pygame.image.load("skeet.png")
# Dave = pygame.image.load('Dave .png')
# img = pygame.image.load("blorenge.png")
# pygame.display.set_icon(img) #sets an icon for the window

# screen = pygame.display.set_mode((1000,1000))
# pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

# yeet_x = 10
# yeet_y = 905
# move = 5
# Skeet_x =879
# Skeet_y =905   
        
        
# running = True
    
        
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_RIGHT]:
#         yeet_x +=move
#     if keys[pygame.K_LEFT]:
#         yeet_x -= move
#     if keys[pygame.K_a]:
#         Skeet_x -= move
#     if keys[pygame.K_d]:
#         Skeet_x += move
#     screen.blit(img, (1,1))
#     screen.blit(Dave, (450,10))
#     screen.blit(yeet, (yeet_x,yeet_y))
#     screen.blit(Skeet, (Skeet_x,Skeet_y))
#     pygame.display.update()














# class Game():
#     def __init__(self):
#         pygame.init()
#         self.yeet = pygame.image.load("yeet.png")
#         self.Skeet = pygame.image.load("skeet.png")
#         self.Dave = pygame.image.load('Dave .png')
#         self.img = pygame.image.load("blorenge.png")
#         pygame.display.set_icon(self.img) #sets an icon for the window

#         self.screen = pygame.display.set_mode((1000,1000))
#         pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

        
        
        
#         running = True
    
        
#         while running:
#             self.screen.blit(self.img, (500,500)) #replace img with an image the size
#                                     #of the screen to serve as background
#             self.screen.blit(self.yeet, (10, 870))
#             self.screen.blit(self.Skeet, (879, 870))
#             self.screen.blit(self.Dave, (450, 10))
#             # for event in pygame.event.get():
#             #     if event.type == pygame.QUIT:
#             #         running = False

#             pygame.display.update() 


    # def skeet_left(self):
    #     skeet_posx = 879
    #     skeet_posy = 870
    #     step_skeetx = 10
    #     step_skeety = 10
    #     if skeet_posx>screen_width-64 or skeet_posx<0:
    #         step_skeetx = -step_skeetx
    #     if skeet_posy>screen_height-64 or skeet_posy<0:
    #         step_skeety = -step_skeety

    #     skeet_posx += step_skeetx
    #     skeet_posy += step_skeety
            
        # def start(self):
        #     while self.running:
        #         self.screen.blit(self.img, (500,500)) #replace img with an image the size of the screen to serve as background
            
            
        #     #self.yeet_left()
            
        #     #self.screen.blit(self.yeet, (50, 870))

        #     #self.screen.blit(self.skeet, (870, 870))
        #         for event in pygame.event.get():
        #             if event.type == pygame.QUIT:
        #                 self.running = False

        #             if event.type == pygame.KEYDOWN:
        #                 if event.key == pygame.K_A:
        #                     pass
        #                 if event.key == pygame.K_D:
        #                     self.skeet_right()





# blit(avatar(x,y))


# class yeet(Sprite):

#    def __init__(self, screen, img_filename, init_pos, init_dir, speed):
#        Sprite.__init__(self)

#        self.image = pygame.Surface([width, height])
#        self.image.fill(color)

#        self.rect = self.image.get_rect()
#        self.char_img = pygame.image.load("Copy of yeet.jpg")
#        self.image = self.char_img
