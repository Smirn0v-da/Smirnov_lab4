import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

def draw_man(surface, x, y, width, height):
    '''
    Функция рисует мужчину
    surface - объект pygame.Surface
    x, y - координаты самой нижней средней точки, от которой будет нарисован мужчина
    wight, height - ширина тела и высота человека 
    '''
    
    def draw_mans_body(surface, x, y, width, height, color):
        '''
        Функция рисует тело
        surface - объект pygame.Surface
        x, y - координаты нижней точки тела
        wight, height - ширина и высота
        color - цвет изображения 
        '''
        ellipse(surface, color, (x - width // 2, y - height, width, height)) 
        
    def draw_mans_head(surface, x, y, width, color):
        '''
        Функция рисует голову
        surface - объект pygame.Surface
        x, y - координаты нижней точки головы
        wight - диаметр
        color - цвет изображения 
        '''
        circle(surface, color, (x, y - width // 2), width // 2)
    
    def draw_mans_hands(surface, x, y, width, cos, length, color):
        '''
        Функция рисует руки
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине между плечами
        width - ширина туловища
        length - длина руки
        cos - косинус угла наклона рук
        color - цвет изображения 
        '''
        line(surface, color, (x - width // 3, y), (x - width // 3 - length * cos, y + length / cos))
        line(surface, color, (x + width // 3, y), (x + width // 3 + length * cos, y + length / cos))
        
    def draw_mans_legs(surface, x, y, width, height, length, color):
        '''
        Функция рисует ноги
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине тела на высоте начала ног
        width - ширина тела
        height - высота ног
        length - длина ступни
        color - цвет изображения
        '''
        lines(surface, color, False, [(x - width // 4, y), (x - width // 4, y + height), (x - width // 4 - length, y + height)])
        lines(surface, color, False, [(x + width // 4, y), (x + width // 4, y + height), (x + width // 4 + length, y + height)])

    body_y = y - height * 2 // 3
    body_color = (128, 128, 128)
    body_height = height // 2
    head_y = y - height * 3 // 4
    head_width = height // 4
    head_color = (255, 222, 173)
    hands_y = body_y - body_height * 0.8
    hands_cos = 0.5
    hands_length = height // 3
    hands_color = (0, 0, 0)
    legs_y = body_y - body_height // 5
    legs_height = y - legs_y
    legs_length = legs_height // 4
    legs_color = (0, 0, 0)

    draw_mans_body(surface, x, body_y, width, body_height)
    draw_mans_head(surface, x, head_y, head_width, head_color)
    draw_mans_hands(surface, x, hands_y, width, hands_cos, hands_length, hands_color)
    draw_mans_legs(surface, x, legs_y, width, legs_height, legs_length, legs_color)
    

def draw_woman(surface, x, y, width, height):
    '''
    '''
    def draw_womans_head(surface, x, y, width, height, color):
        '''
        '''
        pass
    def draw_womans_body(surface, x, y, width, height, color):
        '''
        '''
        pass
    def draw_womans_hands(surface, x, y, width, height, color):
        '''
        '''
        pass
    def draw_womans_legs(surface, x, y, width, height, color):
        '''
        '''
        pass
    pass

def draw_icecream(surface, x, y, width, height):
    '''
    '''
    pass

def draw_balloon(surface, x, y, width, height, color):
    '''
    '''
    pass

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
