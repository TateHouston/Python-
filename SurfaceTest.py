import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()



pygame.display.update()
clock.tick(60)

pygame.quit()
quit()
