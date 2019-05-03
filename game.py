import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite
from random import randint

num = randint(1,2)



num = 1


if num == 1:
    pygame.init()
    yeet = pygame.image.load("yeet.png")
    Skeet = pygame.image.load("skeet.png")
    Dave = pygame.image.load('Dave .png')
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
        if keys[pygame.K_RIGHT]:
            yeet_x +=move
        if keys[pygame.K_LEFT]:
            yeet_x -= move



        #DELETE TEMP 
        if keys[pygame.K_DOWN]:
            yeet_y += move
        if keys[pygame.K_UP]:
            yeet_y -= move


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
        screen.blit(Dave, (450,10))
        screen.blit(yeet, (yeet_x,yeet_y))
        screen.blit(Skeet, (Skeet_x,Skeet_y))
        pygame.display.update()
elif num == 2:
    pygame.init()
    yeet = pygame.image.load("yeet.png")
    Skeet = pygame.image.load("skeet.png")
    Dave = pygame.image.load('Dave .png')
    img = pygame.image.load("blorenge.png")
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
        keys = pygame.key.get_pressed()
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