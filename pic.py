import pygame
from pygame.draw import *
import math
import random as r

pygame.init()

FPS = 30


def draw_house(surface, x, y, width, height, window_radius):
    '''
    Функция рисует дом
    surface - объект pygame.Surface
    x, y - координаты нижней центральной точки дома
    width - ширина стены дома
    height - высота дома
    window_radius - радиус окна
    '''

    def draw_wall(surface, x, y, width, height):
        '''
        Функция рисует стену дома
        surface - объект pygame.Surface
        x, y - координаты нижней центральной точки дома
        width, height - ширина и высота стены дома
        '''
        polygon(surface, (255, 165, 0), [(x + width // 2, y), (x + width // 2, y - height),
                                    (x - width // 2, y - height), (x - width // 2, y)])
        polygon(surface, (0, 0, 0), [(x + width // 2, y), (x + width // 2, y - height),
                                    (x - width // 2, y - height), (x - width // 2, y)], 1)

    def draw_roof(surface, x, y, width, height):
        '''
        Функция рисует крышу дома
        surface - объект pygame.Surface
        x, y - координаты нижней центральной точки крыши
        width, height - ширина и высота крыши
        '''
        polygon(surface, (200, 0, 0), [(x + width // 2, y), (x, y - height), (x - width // 2, y)])
        polygon(surface, (0, 0, 0), [(x + width // 2, y), (x, y - height), (x - width // 2, y)], 1)

    def draw_window(surface, x, y, r):
        '''
        Функция рисует окно
        surface - объект pygame.Surface
        x, y - координаты центра окна
        r - радиус окна
        '''
        circle(surface, (173, 216, 230), (x, y), r)
        circle(surface, (255, 255, 255), (x, y), r, 1)
        line(surface, (255, 255, 255), (x, y + r), (x, y - r), 1)
        line(surface, (255, 255, 255), (x - r, y), (x + r, y), 1)

    wall_height = height * 2 // 3
    roof_y = y - wall_height
    roof_width = width + 20
    roof_height = height - wall_height
    window_y = y - height // 3

    #рисование
    draw_wall(surface, x, y, width, wall_height)
    draw_roof(surface, x, roof_y, roof_width, roof_height)
    draw_window(surface, x, window_y, window_radius)


def cloud(x, y, r):
    for i in range(1, 5):
        circle(screen, (255, 255, 255), (x + r * i, y), r)
        circle(screen, (0, 0, 0), (x + i * r, y), r, 1)
    for i in range(1, 3):
        circle(screen, (255, 255, 255), (x + r * (i + 1), y - r), r)
        circle(screen, (0, 0, 0), (x + (i + 1) * r, y - r), r, 1)


def tree(x, y, l, wid, r):
    polygon(screen, (139, 69, 19), ((x, y), (x + wid, y), (x + wid, y + 2 * l),
                                    (x - wid, y + 2 * l), (x - wid, y), (x, y)))
    for k in range(1, 3):
        circle(screen, (0, 255, 0), (x, y - 3 * r), r)
        circle(screen, (0, 0, 0), (x, y - 3 * r), r, 1)
        circle(screen, (0, 255, 0), (x - r, y - 2 * r), r)
        circle(screen, (0, 0, 0), (x - r, y - 2 * r), r, 1)
        circle(screen, (0, 255, 0), (int(x + 0.6 * r), y - 2 * r), r)
        circle(screen, (0, 0, 0), (int(x + 0.6 * r), y - 2 * r), r, 1)
        y += int(1.5 * r)


screen = pygame.display.set_mode((800, 600))
rect(screen, (135, 206, 250), (0, 0, 800, 350))
rect(screen, (0, 255, 127), (0, 350, 800, 250))
draw_house(screen, 150, 430, 220, 225, 45)
tree(550, 270, 60, 15, 40)
tree(700, 290, 65, 14, 39)
tree(480, 300, 55, 13, 37)
draw_house(screen, 380, 520, 200, 180, 35)
cloud(200, 100, 35)
cloud(580, 90, 40)
cloud(50, 50, 25)



#sun(100, 100, 255, 255, 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
