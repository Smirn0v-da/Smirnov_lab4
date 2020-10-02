import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

def draw_man(surface, x, y, width, height):
    '''
    '''
    def draw_mans_head(surface, x, y, width, height, color):
        '''
        '''
        pass
    def draw_mans_body(surface, x, y, width, height, color):
        '''
        '''
        pass
    def draw_mans_hands(surface, x, y, width, height, color):
        '''
        '''
        pass
    def draw_mans_hands(surface, x, y, width, height, color):
        '''
        '''
        pass
    pass

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
    def draw_womans_hands(surface, x, y, width, height, color):
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
