# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:00 2021

@author: carols1107
"""

import pygame

Black = (0,0,0)

White = (255,255,255)

red = (255,0,0)
    
pygame.init()


size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('下雪')


snow_list =[]

for i in range(50):
    x=random.randrange(0,400)
    y=random.randrange(0,400)
    snow_list.append([x,y])

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

   
    screen.fill(black)
    for i in range(len(snow_list))
        pygame.draw.circle(screen,white,snow list ,(150,150),2)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


    


