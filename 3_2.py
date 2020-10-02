import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

rect(screen, (0, 255, 255), (0, 0, 800, 300))
rect(screen, (127, 255, 0), (0, 300, 800, 300))
circle(screen, (211, 211, 211), (300, 200), 30)
ellipse(screen, (105, 105, 105), (260, 230, 80, 140))
line(screen, (0, 0, 0), (280, 245), (200, 330))
line(screen, (0, 0, 0), (320, 245), (420, 330))
polygon(screen, (244, 164, 96), [(200, 330), (130, 290), (180, 250)])
circle(screen, (255, 0, 0), (160, 250), 17)
circle(screen, (0, 0, 0), (135, 267), 17)
circle(screen, (255, 255, 255), (135, 238), 17)
lines(screen, (0, 0, 0), False, [(280, 360), (250, 450), (220, 450)])
lines(screen, (0, 0, 0), False, [(320, 355), (330, 450), (360, 450)])

polygon(screen, (255, 0, 255), [(550, 200), (500, 370), (600, 370)])
circle(screen, (211, 211, 211), (550, 200), 30)
lines(screen, (0, 0, 0), False, [(530, 370), (530, 450), (505, 450)])
lines(screen, (0, 0, 0), False, [(570, 370), (570, 450), (595, 450)])
line(screen, (0, 0, 0), (540, 240), (420, 330))
lines(screen, (0, 0, 0), False, [(560, 240), (610, 290), (660, 245)])
line(screen, (0, 0, 0), (658, 255), (680, 165))
polygon(screen, (255, 0, 0), [(680, 165), (665, 100), (715, 110)])
circle(screen, (255, 0, 0), (683, 100), 17)
circle(screen, (255, 0, 0), (702, 103), 17)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
