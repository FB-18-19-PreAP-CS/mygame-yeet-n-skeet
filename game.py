import pygame, sys
from pygame.locals import *

import itertools
from pygame.sprite import Sprite
from random import randint
import math
import time
clock = pygame.time.Clock()
vec = pygame.math.Vector2

class Jump():
    def __init__(self):
        self.yeet = pygame.image.load("yeet transparent.png")
        self.Skeet = pygame.image.load("skeet transparent.png")
        self.yeet.on_ground = True
        self.Skeet.on_ground = True
        #self.yeet.x = 10
        yeet_y = 880
        #self.Skeet.x = 879
        self.Skeet.y = 880

def update_yeet(yeet_v, yeet_y,yeet_jumping):
    #yeet_v = 8
    if yeet_jumping:
        print(yeet_y)
        if yeet_v > 0 :
            f = (0.5 * yeet_v**2)
        else:
            f = -(0.5 * yeet_v**2)
        yeet_y -= f
        yeet_v -= 1 # affects jump path
        if yeet_y >= 500:
            yeet_y = 500
            yeet_jumping = False
            yeet_v = 0

num = 1#randint(1,2)
if num == 1:
    pygame.init()
    # pygame.mixer.music.load('rocketchip_zero_gravity_love.mp3') #music setup
    # pygame.mixer.music.play(-1)
    img = pygame.image.load("level 1 wip.png")
    yeet = pygame.image.load("yeet transparent.png")
    Skeet = pygame.image.load("skeet transparent.png")
    Dave = pygame.image.load('Dave transparent.png')
    img = pygame.image.load("level 1 wip.png")

    pygame.display.set_icon(img) #sets an icon for the window
    pygame.display.set_caption("Yeet 'n' Skeet") #name for the window
    screen = pygame.display.set_mode((1000,1000))

    move = 5
    yeet_x = 10
    yeet_y = 880
    yeet_v = 0 # vertical velocity of yeet
    yeet_on_ground = True
    yeet_jumping = False

    Skeet_x = 879
    Skeet_y = 880
    Skeet_v = 0 # vertical velocity of Skeet
    Skeet_on_ground = True
    Skeet_jumping = False

    running = True

    while running:
        #yeet_update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.mixer.music.stop() #stop music
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not yeet_jumping:
                print('jump')
                yeet_v = 8
                yeet_jumping = True

            # elif event.key == pygame.K_s and Skeet_on_ground == True:
            #     print('skeet jump')

            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            yeet_x +=move
        if keys[pygame.K_LEFT]:
            yeet_x -= move
        if keys[pygame.K_a]:
            Skeet_x -= move
        if keys[pygame.K_d]:
            Skeet_x += move

        if yeet_x <= -10:
            yeet_x += move
        if Skeet_x <= -10:
            Skeet_x += move

        if yeet_x >= 930:
            yeet_x -=move
        if Skeet_x >= 930:    ##having trouble with Skeet right barrier
            Skeet_x -= move

        if yeet_y >= 900:
            yeet_y -= move
        if Skeet_y >= 900:
            Skeet_y -= move

        if yeet_y <=0:
            yeet_y += move
        if Skeet_y <= 0:
            Skeet_y -=move

         ### tree border  
         ### tree border  
        if yeet_x == 400 and yeet_y >= 625: 
            yeet_x -= move 
        if Skeet_x <= 550 and Skeet_x >= 500 and Skeet_y >=625:
            Skeet_x +=move
           
        if Skeet_x >= 400 and Skeet_x<=450 and Skeet_y >= 625: 
            Skeet_x -= move 
        if yeet_x <= 550 and yeet_x >= 500 and yeet_y >=630:
            yeet_x +=move
        #top tree border
        if yeet_y == 625 and yeet_x >= 400 and yeet_x <=550:
            yeet_y -= move
        if Skeet_y == 625 and Skeet_x >= 400 and Skeet_x <=550:
            Skeet_y -= move
        #leaf tree border
        if yeet_y ==680 and yeet_x >= 280 and yeet_x <= 680:
            yeet_y -= move
        if Skeet_y ==680 and Skeet_x >= 280 and Skeet_x <= 680:
            Skeet_y -= move
        ##bottom of leaves
        # if yeet_y >= 833 and yeet_x >=375 and yeet_x <= 680:
        #     yeet_y -= move

        if yeet_y == 600 and yeet_x <=213:
            yeet_y -= move

        # if yeet_y ==618 and yeet_x <=120:
        #     yeet_y -= move

        #top middle
        if yeet_x >= 350 and yeet_x <= 475:
            if yeet_y <= 200 and yeet_y >= 125:
                yeet_y -= move
        if yeet_x >= 350 and yeet_x <= 475:
            if yeet_y <= 250 and yeet_y >= 200:
                yeet_y += move

        if Skeet_x >= 350 and Skeet_x <= 475:
            if Skeet_y <= 200 and Skeet_y >= 125:
                Skeet_y -= move
        if Skeet_x >= 350 and Skeet_x <= 475:
            if Skeet_y <= 250 and Skeet_y >= 200:
                Skeet_y += move
            
        #middle
        if yeet_x >= 350 and yeet_x <= 580:
            if yeet_y <= 480 and yeet_y >= 435:
                yeet_y -= move
        if yeet_x >= 400 and yeet_x <= 593:
            if yeet_y <= 580 and yeet_y >= 435:
                yeet_y += move

        #middle two 
        if yeet_x >= 135 and yeet_x <= 384:
            if yeet_y >= 408 and yeet_y <= 420:
                yeet_y += move
        if yeet_x >= 135 and yeet_x <= 384:
            if yeet_y >= 272 and yeet_y <= 275:
                yeet_y -= move

        if yeet_x >= 605 and yeet_x <= 840:
            if yeet_y >= 400 and yeet_y <= 405:
                yeet_y += move
        if yeet_x >= 605 and yeet_x <= 840:
            if yeet_y >= 283 and yeet_y <= 285:
                yeet_y -= move
        update_yeet(yeet_v, yeet_y,yeet_jumping)
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
    img = pygame.image.load("blorenge background.png")
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
        if keys[pygame.K_s]:
            Skeet_y += move
        if keys[pygame.K_w]:
            Skeet_y -= move

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
        if yeet_x >= 930:
            yeet_x -= move
        if Skeet_x >= 930:
            Skeet_x -= move
        
        
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
