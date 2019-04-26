import pygame, sys
from pygame.locals import *
import itertools
from pygame.sprite import Sprite

class Game():
    def __init__(self):
        pygame.init()
        self.yeet = pygame.image.load("yeet.png")
        #self.yeet_pos = (0,0) 
        self.skeet = pygame.image.load("skeet.png")
        #self.skeet_pos = (870, 870)

        self.img = pygame.image.load("blorenge.png")
        pygame.display.set_icon(self.img) #sets an icon for the window

        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Yeet 'n' Skeet") #name for the window
        
        self.screen.blit(self.yeet, (500,500))

        self.running = True

    def yeet_left(self):  #will change to cover both later. trying Yeet first
        yeet_pos = self.yeet.get_rect()
        self.screen.blit(self.yeet, (yeet_pos[0]-50, yeet_pos[1]))

    def yeet_right(self):
        yeet_pos = self.yeet.get_rect()
        self.screen.blit(self.yeet, (yeet_pos[0]+50, yeet_pos[1]))
        

    def start(self):
        while self.running:
            self.screen.blit(self.img, (500,500)) #replace img with an image the size of the screen to serve as background
            
            
            #self.yeet_left()
            
            #self.screen.blit(self.yeet, (50, 870))

            #self.screen.blit(self.skeet, (870, 870))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.yeet_left()
                    if event.key == pygame.K_RIGHT:
                        self.yeet_right()

                
            pygame.display.update() 


    

def main():
    g = Game()
    #g.yeet_left()
    g.start()

if __name__ == "__main__":
    main()