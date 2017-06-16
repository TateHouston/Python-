#Pygame template
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Grou()



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