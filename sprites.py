import pygame
pygame.init()

screen = pygame.display.set_mode(1000,1000)
class Yeet(pygame.sprite.Sprite):

    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('yeet.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0,0]
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown"

def 
    for event in pygame.event.get():
        if event.type == QUIT:
            return
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                player.moveup()
            if event.key == K_DOWN:
                player.movedown()
        elif event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                player.movepos = [0,0]
                player.state = "still"

run()