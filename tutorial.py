import pygame
pygame.init()

screen = pygame.display.set_mode(500,500)

x = 50
y = 50
w = 40
h = 6
vel =5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += vel
    


    pygame.draw.rect(screen, (0,255,0), (x,y,w, h))
    pygame.display.update() 
