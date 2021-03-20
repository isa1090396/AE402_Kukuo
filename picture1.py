# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:00 2021

@author: carols1107
"""

import pygame

Black = (0,0,0,)

White = (255,255,255)

Green = (0,255,0)

pygame.init()


size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('我的遊戲')

done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(White)
    pygame.draw.polygon(screen,Green,[(350,250),(100,250),(100,50)], 5)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


    


