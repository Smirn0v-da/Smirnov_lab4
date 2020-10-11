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


def draw_cloud(surface, x, y, r):
    '''
    Функция рисует облака
    surface - объект pygame.Surface
    x, y - координаты центра нижнего левого кружка облака 
    r - радиус кружков, из которых состоит облако 
    '''
    for i in range(4):
        circle(screen, (255, 255, 255), (x + r * i, y), r)
        circle(screen, (0, 0, 0), (x + i * r, y), r, 1)
    for i in range(2):
        circle(screen, (255, 255, 255), (x + r * (i + 1), y - r), r)
        circle(screen, (0, 0, 0), (x + (i + 1) * r, y - r), r, 1)


def draw_tree(surface, x, y, width, height, r):
    '''
    Функция рисует дерево
    surface - объект pygame.Surface
    x, y - координаты нижней центральной точки дерева
    width - ширина ствола
    height - высота всего дерева
    r - радиус кружков, из которых состоит крона
    '''
    polygon(screen, (139, 69, 19), [(x + width // 2, y), (x + width // 2, y - height + r * 3),
                                    (x - width // 2, y - height + r * 3), (x - width // 2, y)])
    y -= height - r * 3
    for i in range(2):
        circle(screen, (0, 255, 0), (x, y - 3 * r), r)
        circle(screen, (0, 0, 0), (x, y - 3 * r), r, 1)
        circle(screen, (0, 255, 0), (x - r, y - 2 * r), r)
        circle(screen, (0, 0, 0), (x - r, y - 2 * r), r, 1)
        circle(screen, (0, 255, 0), (int(x + 0.6 * r), y - 2 * r), r)
        circle(screen, (0, 0, 0), (int(x + 0.6 * r), y - 2 * r), r, 1)
        y += r * 3 // 2


screen = pygame.display.set_mode((800, 600))
rect(screen, (135, 206, 250), (0, 0, 800, 350))
rect(screen, (0, 255, 127), (0, 350, 800, 250))
draw_house(screen, 150, 430, 220, 225, 45)
draw_tree(screen, 550, 390, 30, 240, 40)
draw_tree(screen, 700, 420, 28, 247, 39)
draw_tree(screen, 480, 410, 26, 221, 37)
draw_house(screen, 380, 520, 200, 180, 35)
draw_cloud(screen, 235, 100, 35)
draw_cloud(screen, 620, 90, 40)
draw_cloud(screen, 75, 50, 25)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
