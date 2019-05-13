import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite
from random import randint
clock = pygame.time.Clock()
vec = pygame.math.Vector2

# class Animation(Sprite):
#     def __init__(self,frames):
#         pygame.sprite.Sprite.__init__(self)
#         self.frames = frames       # save the images in here
#         self.current = 0       # idx of current image of the animation
#         self.image = frames[0]  # just to prevent some errors
#         self.rect = self.image.get_rect()    # same here
#         self.playing = 0

#     def update(self, *args):
#         if self.playing:    # only update the animation if it is playing
#             self.current += 1
#             if self.current == len(self.frames):
#                 self.current = 0
#             self.image = self.frames[self.current]
#             # only needed if size changes within the animation
#             self.rect = self.image.get_rect(center=self.rect.center)

        
#     def yeet_frames():
#         frames = []
#         for i in range(5):
#             frames.append(pygame.image.load("yeet transparent"+str(i)+".png"))
#         for i in range(5):
#             frames.append(frames[4-i]) # right, using same object twice
#         # this gives [0,1,2,3,4,4,3,2,1,0]

#     def skeet_frames():
#         frames = []
#         for i in range(5):
#             frames.append(pygame.image.load("yeet transparent"+str(i)+".png"))
#         for i in range(5):
#             frames.append(frames[4-i]) # right, using same object twice
#         # this gives [0,1,2,3,4,4,3,2,1,0]


num = 1#randint(1,2)
if num == 1:
    pygame.init()
    # pygame.mixer.music.load('rocketchip_zero_gravity_love.mp3') #music setup
    # pygame.mixer.music.play(-1)
    yeet = pygame.image.load("yeet transparent.png")
    Skeet = pygame.image.load("skeet transparent.png")
    Dave = pygame.image.load('Dave transparent.png')
    img = pygame.image.load("level 1 wip.png")
    pygame.display.set_icon(img) #sets an icon for the window

    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

    move = 5
    yeet_x = 10
    yeet_y = 905
    #yeet_pos = vec(10, 905)
    # yeet_vel = vec(0,0)
    # yeet_acc = vec(0,0)

    Skeet_x = 879
    Skeet_y = 905
    #skeet_pos = vec(875,905)
    # skeet_vel = vec(0,905)
    # skeet_acc = vec(875,0)

    running = True
            
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.mixer.music.stop() #stop music
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yeet_y -= 250
            elif event.key == pygame.K_s:
                Skeet_y -= 250
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                yeet_y += 250
            elif event.key == pygame.K_s:
                Skeet_y += 250
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
            yeet_y+= move
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


        #print(yeet_x, yeet_y)

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
