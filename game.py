import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite
from random import randint
from time import sleep

#class Game():
    # def __init__():
    #     pygame.init()
# class Avatar(pygame.sprite.Sprite):
#     def __init__(self, width, height):
#         pygame.sprite.Sprite.__init__(self)

#         self.image = pygame.Surface([width, height])
#         self.image.fill('white')
#         self.rect = self.image.get_rect()
WHITE = (255,255,255)
BLACK = (0,0,0)

font_name = pygame.font.match_font('arial')
def display_text(surf, text, size, x, y,color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit (text_surface, text_rect)


num = 1#randint(1,2)
if num == 1:
    pygame.init()
    yeet = pygame.image.load("yeet transparent.png")
    Skeet = pygame.image.load("skeet transparent.png")
    Dave = pygame.image.load('Dave transparent.png')
    img = pygame.image.load("level 1 wip.png")
    coin = pygame.image.load("coin.png")
    Skeet_win = pygame.image.load("skeet wins.png")
    yeet_win = pygame.image.load("yeet wins.png")
    pygame.display.set_icon(img) #sets an icon for the window

    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

    yeet_x = 10
    yeet_y = 905
    move = 5
    Skeet_x =879
    Skeet_y =905   

    coins = [(465,430), (250,275), (605,285), (10, 355), (925, 350)]
    coins_2 = [(465,430), (145,595), (805,600), (475,620), (420,115)]
    coins_3 = [(360, 675), (635, 460), (20,55), (880, 75),(405,425)]

    c = 3 #randint(1,3)

    yeet_score = 0
    Skeet_score = 0
            
    is_dave = False

    running = True
        
            
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"{yeet_x} {yeet_y}")
        keys = pygame.key.get_pressed()
        
        #temp yeet controls
        if keys[pygame.K_DOWN]:
            Skeet_y += move
        if keys[pygame.K_UP]:
            Skeet_y -= move
            
        if keys[pygame.K_s]:
            yeet_y += move
        if keys[pygame.K_w]:
            yeet_y -= move
        
        if keys[pygame.K_RIGHT]:
            Skeet_x +=move
        if keys[pygame.K_LEFT]:
            Skeet_x -= move
        if keys[pygame.K_a]:
            yeet_x -= move
        if keys[pygame.K_d]:
            yeet_x += move
            
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
            Skeet_y +=move




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
        if yeet_y == 830 and yeet_x >= 285 and yeet_x <= 655:
            yeet_y += move
        ##Trunks left side
        if yeet_y == 600 and yeet_x <=213:
            yeet_y -= move

        if yeet_y == 520 and yeet_x <= 90:
            yeet_y -= move
        
        if yeet_y == 755 and yeet_x <= 170:
            yeet_y += move

        if yeet_y == 360 and yeet_x <= 5:
            yeet_y -= move
        
        if yeet_y == 210 and yeet_x <= 45:
            yeet_y += move
        if yeet_y == 245 and yeet_x >= 45 and yeet_x <= 240:
            yeet_y += move
        if yeet_y == 115 and yeet_x <= 235:
            yeet_y -= move
        if yeet_y == 60 and yeet_x <= 100:
            yeet_y -= move
        
        ##Trunks right side
        if yeet_y == 745 and yeet_x >=775:
            yeet_y += move
        if yeet_y == 605 and yeet_x >=775:
            yeet_y -= move
        if yeet_y == 515 and yeet_x >= 845:
            yeet_y -= move
        if yeet_y == 355 and yeet_x >= 925:
            yeet_y -= move
        if yeet_y == 220 and yeet_x >=880:
            yeet_y += move
        if yeet_y == 260 and yeet_x >=655 and yeet_x <= 855:
            yeet_y += move
        if yeet_y == 125 and yeet_x >= 650:
            yeet_y -= move
        if yeet_y == 80 and yeet_x >= 805:
            yeet_y -= move
        
        #### SKEET BORDERS ######

        ##bottom of leaves
        if Skeet_y == 830 and Skeet_x >= 285 and Skeet_x <= 655:
            Skeet_y += move
        ##Trunks left side
        if Skeet_y == 600 and Skeet_x <=213:
            Skeet_y -= move

        if Skeet_y == 520 and Skeet_x <= 90:
            Skeet_y -= move
        
        if Skeet_y == 755 and Skeet_x <= 170:
            Skeet_y += move

        if Skeet_y == 360 and Skeet_x <= 5:
            Skeet_y -= move
        
        if Skeet_y == 210 and Skeet_x <= 45:
            Skeet_y += move
        if Skeet_y == 245 and Skeet_x >= 45 and Skeet_x <= 240:
            Skeet_y += move
        if Skeet_y == 115 and Skeet_x <= 235:
            Skeet_y -= move
        if Skeet_y == 60 and Skeet_x <= 100:
            Skeet_y -= move
        
        ##Trunks right side
        if Skeet_y == 745 and Skeet_x >=775:
            Skeet_y += move
        if Skeet_y == 605 and Skeet_x >=775:
            Skeet_y -= move
        if Skeet_y == 515 and Skeet_x >= 845:
            Skeet_y -= move
        if Skeet_y == 355 and Skeet_x >= 925:
            Skeet_y -= move
        if Skeet_y == 220 and Skeet_x >=880:
            Skeet_y += move
        if Skeet_y == 260 and Skeet_x >=655 and Skeet_x <= 855:
            Skeet_y += move
        if Skeet_y == 125 and Skeet_x >= 650:
            Skeet_y -= move
        if Skeet_y == 80 and Skeet_x >= 805:
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
            
        #middle 
        if yeet_y == 475 and yeet_x >= 230 and yeet_x<=710:
            yeet_y -= move
        if yeet_y == 435 and yeet_x >=365 and yeet_x <= 555:
            yeet_y -= move
        if yeet_y == 590 and yeet_x >=240 and yeet_x <=375:
            yeet_y += move
        if yeet_y == 570 and yeet_x >= 375 and yeet_x <= 555:
            yeet_y += move
        if yeet_y == 590 and yeet_x >= 555 and yeet_x <= 705:
            yeet_y += move
        

        #middle two 
        if yeet_y == 290 and yeet_x >=570 and yeet_x<=800:
            yeet_y -= move
        if yeet_y == 420 and yeet_x >= 570 and yeet_x <= 800:
            yeet_y += move
        
        if yeet_y == 280 and yeet_x >=100 and yeet_x <= 345:
            yeet_y -= move
        if yeet_y == 415 and yeet_x >= 110 and yeet_x <= 340:
            yeet_y += move
        

        #middle Skeet
        if Skeet_y == 475 and Skeet_x >= 230 and Skeet_x<=710:
            Skeet_y -= move
        if Skeet_y == 435 and Skeet_x >=365 and Skeet_x <= 555:
            Skeet_y -= move
        if Skeet_y == 590 and Skeet_x >=240 and Skeet_x <=375:
            Skeet_y += move
        if Skeet_y == 570 and Skeet_x >= 375 and Skeet_x <= 555:
            Skeet_y += move
        if Skeet_y == 590 and Skeet_x >= 555 and Skeet_x <= 705:
            Skeet_y += move
        

        #middle two Skeet 

        if Skeet_y == 290 and Skeet_x >=570 and Skeet_x<=800:
            Skeet_y -= move
        if Skeet_y == 420 and Skeet_x >= 570 and Skeet_x <= 800:
            Skeet_y += move
        
        if Skeet_y == 280 and Skeet_x >=100 and Skeet_x <= 345:
            Skeet_y -= move
        if Skeet_y == 415 and Skeet_x >= 110 and Skeet_x <= 340:
            Skeet_y += move

        yeet_coord = (yeet_x, yeet_y)
        Skeet_coord = (Skeet_x+1, Skeet_y)
        Dave_coord = (450,10)
        screen.blit(img, (1,1))
        screen.blit(Dave, (450,10))
        screen.blit(yeet, (yeet_x,yeet_y))
        screen.blit(Skeet, (Skeet_x,Skeet_y))
        display_text(screen, f'Yeet Score:{yeet_score}', 28, 155, 10, WHITE)
        display_text(screen, f'Skeet Score:{Skeet_score}', 28, 810, 10, WHITE)
        # screen.blit(coin, coins[0])
        # screen.blit(coin, coins[1])
        # screen.blit(coin, coins[2])
        # screen.blit(coin, coins[3])
        # screen.blit(coin, coins[4])

        # for i in range(len(coins)):
        #     yeet_coord = (yeet_x, yeet_y)
        #     if coins[i] == yeet_coord:
        #         del coins[i]
        #     elif yeet_coord != coins[i]:
        #         screen.blit(coin, coins[i])
        

        i = 0
    
        if c ==1:
            if len(coins_2) > 0:
                for ele in coins:
                    if coins[i] == yeet_coord:
                        yeet_score += 1
                        del coins[i]


                    elif yeet_coord != coins[i] and Skeet_coord != coins[i]:
                        screen.blit(coin, coins[i])
                    i += 1 
        i =0
        if c == 1:
            if len(coins_2) > 0:
                for ele in coins:                    
                    if coins[i] == Skeet_coord:
                        Skeet_score += 1
                        del coins[i]
                    elif yeet_coord != coins[i] and Skeet_coord != coins[i]:
                        screen.blit(coin, coins[i])
                    i += 1

        if c == 2:
            if len(coins_2) > 0:
                for ele in coins_2:
                    yeet_coord = (yeet_x, yeet_y)
                    Skeet_coord = (Skeet_x+1, Skeet_y)

                    if coins_2[i] == Skeet_coord:
                        Skeet_score += 1
                        del coins_2[i]
                    elif yeet_coord != coins_2[i] and Skeet_coord != coins_2[i]:
                        screen.blit(coin, coins_2[i])
                    i += 1
        
        i = 0
        if c == 2:
            if len(coins_2) > 0:
                for ele in coins_2:
                    yeet_coord = (yeet_x, yeet_y)
                    Skeet_coord = (Skeet_x, Skeet_y)
                    if coins_2[i] == yeet_coord:
                        yeet_score += 1
                        del coins_2[i]
                    elif yeet_coord != coins_2[i] and Skeet_coord != coins_2[i]:
                        screen.blit(coin, coins_2[i])
                    i += 1
        
        if c == 3:
            if len(coins_3) > 0:
                for ele in coins_2:
                    yeet_coord = (yeet_x, yeet_y)
                    Skeet_coord = (Skeet_x+1, Skeet_y)

                    if coins_3[i] == Skeet_coord:
                        Skeet_score += 1
                        del coins_3[i]
                    elif yeet_coord != coins_3[i] and Skeet_coord != coins_3[i]:
                        screen.blit(coin, coins_3[i])
                    i += 1

        i = 0
        if c == 3:
            if len(coins_3) > 0:
                for ele in coins_3:
                    yeet_coord = (yeet_x, yeet_y)
                    Skeet_coord = (Skeet_x, Skeet_y)
                    if coins_3[i] == yeet_coord:
                        yeet_score += 1
                        del coins_3[i]
                    elif yeet_coord != coins_3[i] and Skeet_coord != coins_3[i]:
                        screen.blit(coin, coins_3[i])
                    i += 1

        if is_dave == False:
            if Skeet_x >= 405 and Skeet_y == 5:
                Skeet_score += 2
                is_dave = True
                if is_dave == True:
                    if Skeet_score > yeet_score:
                        
                        #screen.blit(Skeet_win, (1,1))
                        running = False
                        #sleep(5)

                        

            if yeet_x >= 405 and yeet_y == 5:
                yeet_score += 2
                is_dave = True
                if is_dave == True:
                    if yeet_score > Skeet_score:
                        #screen.blit(yeet_win, (1,1))
                        running = False
                
        
        
        
        pygame.display.update()
    if Skeet_score > yeet_score:
        screen.blit(Skeet_win, (1,1))
        display_text(screen, f'Skeet won with a score of:{Skeet_score}', 40, 500, 150,BLACK)
        display_text(screen, f'THANK YOU FOR PLAYING!', 40, 500, 240,BLACK)
        pygame.display.update()
        sleep(5)
    if yeet_score > Skeet_score:
        screen.blit(yeet_win, (1,1))
        display_text(screen, f'Yeet won with a score of:{yeet_score}', 40, 500, 150,BLACK)
        display_text(screen, f'THANK YOU FOR PLAYING!', 40, 500, 240,BLACK)
        pygame.display.update()
        sleep(5)

# elif num == 2:
#     pygame.init()
#     yeet = pygame.image.load("yeet transparent.png")
#     Skeet = pygame.image.load("skeet transparent.png")
#     Dave = pygame.image.load('Dave transparent.png')
#     img = pygame.image.load("blorenge background.png")
#     pygame.display.set_icon(img) #sets an icon for the window

#     screen = pygame.display.set_mode((1000,1000))
#     pygame.display.set_caption("Yeet 'n' Skeet") #name for the window

#     yeet_x = 10
#     yeet_y = 905
#     move = 5
#     Skeet_x =879
#     Skeet_y =905   
        
        
#     running = True
    
        
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         keys = pygame.key.get_pressed()
        
#         #temp yeet controls
#         if keys[pygame.K_s]:
#             Skeet_y += move
#         if keys[pygame.K_w]:
#             Skeet_y -= move

#         if keys[pygame.K_DOWN]:
#             yeet_y += move
#         if keys[pygame.K_UP]:
#             yeet_y -= move
        
#         if keys[pygame.K_RIGHT]:
#             yeet_x +=move
#         if keys[pygame.K_LEFT]:
#             yeet_x -= move
#         if keys[pygame.K_a]:
#             Skeet_x -= move
#         if keys[pygame.K_d]:
#             Skeet_x += move
            
#         if yeet_x <= 0:
#             yeet_x += move
#         if Skeet_x <= 0:
#             Skeet_x += move
#         if yeet_x >= 930:
#             yeet_x -= move
#         if Skeet_x >= 930:
#             Skeet_x -= move
        
        
#         screen.blit(img, (1,1))
#         screen.blit(Dave, (50,10))
#         screen.blit(yeet, (yeet_x,yeet_y))
#         screen.blit(Skeet, (Skeet_x,Skeet_y))
#         pygame.display.update()



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
