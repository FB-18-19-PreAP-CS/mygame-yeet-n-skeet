import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite

pygame.init()

screen = pygame.display.set_mode((1000,1000))
yeet = pygame.image.load("yeet.png")
yeet_x = 50
yeet_y = 50
move = 5 #how many pixels it moves

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        yeet_x += move
    if keys[pygame.K_LEFT]:
        yeet_x -= move
    
    screen.fill((255,255,255)) #replace with bg
    screen.blit(yeet, (yeet_x,yeet_y))
    pygame.display.update() 



# class Game():
#     def __init__(self):
#         pygame.init()
#         self.yeet = pygame.image.load("yeet.png")
#         self.yeet_pos = self.yeet.get_rect()
#         #self.yeet_pos = pygame.rect.Rect((0,0,0,0))
#         self.skeet = pygame.image.load("skeet.png")
#         self.img = pygame.image.load("blorenge.png")
#         pygame.display.set_icon(self.img) #sets an icon for the window

#         self.screen = pygame.display.set_mode((1000,1000))
#         pygame.display.set_caption("Yeet 'n' Skeet") #name for the window
        
#         self.screen.blit(self.yeet, (500,500))

#         self.running = True


#     def yeet_left(self):  #will change to cover both later. trying Yeet first
#         yeet_pos = self.yeet.get_rect()
#         self.screen.blit(self.yeet, (yeet_pos[0]-50, yeet_pos[1]))

#     def yeet_right(self, yeet_pos):
#         #yeet_pos = self.yeet.get_rect()
#         self.screen.blit(self.yeet, (self.yeet_pos[0]+50, self.yeet_pos[1]))
#         print(self.yeet.get_rect())
        

#     def start(self):
#         while self.running:
#             self.screen.blit(self.img, (500,500)) #replace img with an image the size of the screen to serve as background
#             #self.screen.blit(self.yeet, (50, 870))

#             #self.screen.blit(self.skeet, (870, 870))
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False

#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         #yeet_pos = self.yeet.get_rect()
#                         self.yeet_left()
#                     if event.key == pygame.K_RIGHT: 
#                         yeet_pos = self.yeet.get_rect()
                        
#                         #print()
#                         #self.yeet_right(self.yeet_pos)
#             self.screen.blit(self.img, (500,500))
#             #self.draw_yee()
#             pygame.display.update() 


    

# def main():
#     g = Game()
#     #g.yeet_left()
#     g.start()

# if __name__ == "__main__":
#     main()