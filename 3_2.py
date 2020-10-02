import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

def draw_man(surface, x, y, height, k_left, k_right):
    '''
    Функция рисует мужчину
    surface - объект pygame.Surface
    x, y - координаты самой нижней средней точки, от которой будет нарисован мужчина
    height - высота человека
    k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая 
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
    
    def draw_mans_hands(surface, x, y, width, cos, length, color, k_left, k_right):
        '''
        Функция рисует руки
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине между плечами
        width - ширина туловища
        length - длина руки
        cos - косинус угла наклона рук
        color - цвет изображения
        k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая 
        '''
        sin = (1 - cos ** 2) ** (1 / 2)
        lines(surface, color, False, [(x - width // 4, y), (x - width // 4 - int(length * cos) // 2, y + int(length * sin) // 2), 
                                      (x - width // 4 - int(length * cos), y + int(length * sin) * k_left)])
        lines(surface, color, False, [(x + width // 4, y), (x + width // 4 + int(length * cos) // 2, y + int(length * sin) // 2),
                                      (x + width // 4 + int(length * cos), y + int(length * sin) * k_right)])
        
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
        a = 0.2 #случайный параметр для наклона ноги ( при a = 0 наклон отсутствует)
        lines(surface, color, False, [(x - width // 4, y), (x - width // 4 - int(a * height), y + height), (x - width // 4 - int(a * height)  - length, y + height)])
        lines(surface, color, False, [(x + width // 4, y), (x + width // 4, y + height), (x + width // 4 + length, y + height)])

    #ширина человека
    width = height // 4
    #тело
    body_y = y - height // 3
    body_color = (128, 128, 128)
    body_height = height // 2
    #голова 
    head_y = y - height * 4 // 5
    head_width = height // 5
    head_color = (255, 222, 173)
    #руки
    hands_y = int(body_y - body_height * 0.9)
    hands_cos = 0.5
    hands_length = height // 3
    hands_color = (0, 0, 0)
    #ноги
    legs_y = body_y - body_height // 10
    legs_height = y - legs_y
    legs_length = legs_height // 4
    legs_color = (0, 0, 0)

    #непосредственно рисование 
    draw_mans_body(surface, x, body_y, width, body_height, body_color)
    draw_mans_head(surface, x, head_y, head_width, head_color)
    draw_mans_hands(surface, x, hands_y, width, hands_cos, hands_length, hands_color, k_left, k_right)
    draw_mans_legs(surface, x, legs_y, width, legs_height, legs_length, legs_color)
    

def draw_woman(surface, x, y, height, k_left, k_right):
    '''
    Функция рисует женщину
    surface - объект pygame.Surface
    x, y - координаты самой нижней средней точки, от которой будет нарисована женщина
    k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая
    height - высота человека 
    '''
    
    def draw_womans_body(surface, x, y, width, height, color):
        '''
        Функция рисует тело
        surface - объект pygame.Surface
        x, y - координаты нижней точки тела
        wight, height - ширина и высота
        color - цвет изображения 
        '''
        polygon(surface, color, [(x, y - height), (x + width // 2, y), (x - width // 2, y)])
        
    def draw_womans_head(surface, x, y, width, color):
        '''
        Функция рисует голову
        surface - объект pygame.Surface
        x, y - координаты нижней точки головы
        wight - диаметр
        color - цвет изображения 
        '''
        circle(surface, color, (x, y - width // 2), width // 2)
    
    def draw_womans_hands(surface, x, y, width, cos, length, color, k_left, k_right):
        '''
        Функция рисует руки
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине между плечами
        width - ширина туловища
        length - длина руки
        cos - косинус угла наклона рук
        color - цвет изображения
        k - параметр для сгиба рук. При k = 1 рука прямая, при 0 - согнутая
        '''
        sin = (1 - cos ** 2) ** (1 / 2) #считаем синус угла
        lines(surface, color, False, [(x - width // 8, y), (x - width // 8 - int(length * cos) // 2, y + int(length * sin) // 2), 
                                      (x - width // 8 - int(length * cos), y + int(length * sin) * k_left)])
        lines(surface, color, False, [(x + width // 8, y), (x + width // 8 + int(length * cos) // 2, y + int(length * sin) // 2),
                                      (x + width // 8 + int(length * cos), y + int(length * sin) * k_right)])
        
    def draw_womans_legs(surface, x, y, width, height, length, color):
        '''
        Функция рисует ноги
        surface - объект pygame.Surface
        x, y - координаты точки, находящейся посередине тела на высоте начала ног
        width - ширина тела
        height - высота ног
        length - длина ступни
        color - цвет изображения
        '''
        lines(surface, color, False, [(x - width // 6, y), (x - width // 6, y + height), (x - width // 6 - length, y + height)])
        lines(surface, color, False, [(x + width // 6, y), (x + width // 6, y + height), (x + width // 6 + length, y + height)])

    #ширина человека
    width = height // 3
    #тело
    body_y = y - height // 3
    body_color = (255, 0, 255)
    body_height = int(height // 1.75)
    #голова 
    head_y = y - height * 4 // 5
    head_width = height // 5
    head_color = (255, 222, 173)
    #руки
    hands_y = int(body_y - body_height * 0.8)
    hands_cos = 0.5
    hands_length = int(height // 2.5)
    hands_color = (0, 0, 0)
    #ноги
    legs_y = body_y
    legs_height = y - legs_y
    legs_length = legs_height // 4
    legs_color = (0, 0, 0)

    #непосредственно рисование 
    draw_womans_body(surface, x, body_y, width, body_height, body_color)
    draw_womans_head(surface, x, head_y, head_width, head_color)
    draw_womans_hands(surface, x, hands_y, width, hands_cos, hands_length, hands_color, k_left, k_right)
    draw_womans_legs(surface, x, legs_y, width, legs_height, legs_length, legs_color) 

def draw_icecream(surface, x, y, width, height):
    '''
    '''
    pass

def draw_balloon(surface, x, y, width, height, color):
    '''
    '''
    pass

rect(screen, (255, 255, 255), (0, 0, 800, 600))
draw_man(screen, 200, 500, 450, 1, 1)
draw_woman(screen, 400, 500, 450, 1, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
