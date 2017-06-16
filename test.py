#Pygame template
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Player(pygame.sprite.Sprite):
    #Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH /2
        self.rect.bottom - HEIGHT -10

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right =0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


#Game Loop
running = True
while running:
    #Keep loop running at right speed
    clock.tick(FPS)
    #Process Input
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()

    #Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()