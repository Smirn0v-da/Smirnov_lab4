import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (192, 192, 192), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (160, 175), 20)
circle(screen, (255, 0, 0), (240, 175), 15)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (0, 0, 0), (160, 175), 20, 1)
circle(screen, (0, 0, 0), (240, 175), 15, 1)
circle(screen, (0, 0, 0), (160, 175), 10)
circle(screen, (0, 0, 0), (240, 175), 8)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
polygon(screen, (0, 0, 0) ,[(100, 110), (190, 160), (185, 170), (95, 120)])
polygon(screen, (0, 0, 0) ,[(210, 160), (215, 170), (300, 135), (295, 125)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
