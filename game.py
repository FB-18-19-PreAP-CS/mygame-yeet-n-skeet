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
    Skeet_x = 879
    Skeet_y = 905   

            

    running = True
        
            
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(yeet_x, yeet_y)
                
                
        keys = pygame.key.get_pressed()
        
        #temp yeet controls
        if keys[pygame.K_DOWN]:
            yeet_y += move
        if keys[pygame.K_UP]:
            yeet_y -= move
        if keys[pygame.K_s]:
            Skeet_y += move
        if keys[pygame.K_w]:
            Skeet_y -= move
        
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
            yeet_x -= move
        if Skeet_x >= 930:
            Skeet_x -= move
            
        if yeet_y <= 0:
            yeet_y += move
        if yeet_y >= 900:
            yeet_y -= move
        if Skeet_y <= 0:
            Skeet_y += move
        if Skeet_y >= 900:
            Skeet_y -= move

        #top middle Yeet
        if yeet_x >= 350 and yeet_x <= 510:
            if yeet_y <= 200 and yeet_y >= 125:
                yeet_y -= move
        if yeet_x >= 350 and yeet_x <= 510:
            if yeet_y <= 250 and yeet_y >= 200:
                yeet_y += move

        if yeet_x == 345: 
            if yeet_y <= 255 and yeet_y >= 115:
                yeet_x -= move
        if yeet_x == 515:
            if yeet_y <= 255 and yeet_y >= 115:
                yeet_x += move

        #top middle Skeet
        if Skeet_x >= 350 and Skeet_x <= 475:
            if Skeet_y <= 200 and Skeet_y >= 125:
                Skeet_y -= move
        if Skeet_x >= 350 and Skeet_x <= 490:
            if Skeet_y <= 250 and Skeet_y >= 200:
                Skeet_y += move
        if Skeet_x == 345: 
            if Skeet_y <= 255 and Skeet_y >= 115:
                Skeet_x -= move
        if Skeet_x == 515:
            if Skeet_y <= 160 and Skeet_y >= 115:
                Skeet_x += move
            
        #middle ##A few borders do not work
        if yeet_x >= 350 and yeet_x <= 580:
            if yeet_y <= 480 and yeet_y >= 435:
                yeet_y -= move
        if yeet_x >= 400 and yeet_x <= 593:
            if yeet_y <= 570 and yeet_y >= 565:
                yeet_y += move

        if yeet_x >= 235 and yeet_x <= 715:
            if yeet_y == 465:
                yeet_y -= move
        if yeet_x >= 235 and yeet_x <= 595:
            if yeet_y == 595:
                yeet_y += move

        if yeet_x == 585:
            if yeet_y >= 430 and yeet_y <= 460:
                yeet_y +=  move

        if yeet_x == 735:
            if yeet_y >= 555 and yeet_y <= 590:
                yeet_x == 740

        if yeet_x >= 210 and yeet_x <= 630:
            if yeet_y >= 460 and yeet_y <= 585:
                yeet_x -= move

        if yeet_x >= 555 and yeet_x <= 715:
            if yeet_y == 595:
                yeet_y += move
        

        #middle two ###a few borders do not work
        # if yeet_x >= 85 and yeet_x <= 355:
        #     if yeet_y == 420:
        #         yeet_y += move
        # if yeet_x >= 85 and yeet_x <= 355:
        #     if yeet_y >= 272 and yeet_y <= 275:
        #         yeet_y -= move

        if yeet_x == 550:
            if yeet_y >= 285 and yeet_y < 420:
                yeet_x -= move
        if yeet_x <= 825 and yeet_x >= 775:
            if yeet_y >= 280 and yeet_y <= 330:
                yeet_x += move

        if yeet_x >= 560 and yeet_x <= 810:
            if yeet_y == 420:
                yeet_y += move
        if yeet_x >= 560 and yeet_x <= 810:
            if yeet_y >= 283 and yeet_y <= 285:
                yeet_y -= move

        #middle Skeet
        # if Skeet_y == 468 and Skeet_x >=240 and Skeet_x<= 330:
        #     Skeet_y -=move

        # if Skeet_x >= 350 and Skeet_x <= 580:
        #     if Skeet_y <= 480 and Skeet_y >= 435:
        #         Skeet_y -= move
        # if Skeet_x >= 400 and Skeet_x <= 593:
        #     if Skeet_y <= 570 and Skeet_y >= 565:
        #         Skeet_y += move

        # if Skeet_x >= 235 and Skeet_x <= 715:
        #     if Skeet_y == 465:
        #         Skeet_y -= move
        # if Skeet_x >= 235 and Skeet_x <= 595:
        #     if Skeet_y == 595:
        #         Skeet_y += move

        # if Skeet_x == 585:
        #     if Skeet_y >= 430 and Skeet_y <= 460:
        #         Skeet_y +=  move

        # if Skeet_x == 735:
        #     if Skeet_y >= 555 and Skeet_y <= 590:
        #         Skeet_x == 740

        # if Skeet_x >= 210 and Skeet_x <= 630:
        #     if Skeet_y >= 460 and Skeet_y <= 585:
        #         Skeet_x -= move

        # if Skeet_x >= 555 and Skeet_x <= 715:
        #     if Skeet_y == 595:
        #         Skeet_y += move

        #middle two Skeet ##works, no side borders tho

        if Skeet_y == 290 and Skeet_x >=570 and Skeet_x<=800:
            Skeet_y -= move
        if Skeet_y == 420 and Skeet_x >= 570 and Skeet_x <= 800:
            Skeet_y += move
        
        if Skeet_y == 280 and Skeet_x >=100 and Skeet_x <= 345:
            Skeet_y -= move
        if Skeet_y == 415 and Skeet_x >= 110 and Skeet_x <= 340:
            Skeet_y += move
        



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
            yeet_y += move
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
