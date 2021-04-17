# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:00 2021

@author: carols1107
"""

import pygame,random

Black = (0,0,0)
White = (255,255,255)
RED=(255, 0, 0)     
pygame.init()
           
Screen_w =700
Screen_h =400
screen = pygame.display.set_mode([Screen_w,Screen_h])


player_x = 0
player_y = 0
player_w = 50
player_h = 50

block_w = 50
block_h = 50
block_x = []
block_y = []
Hit = []
for i in range(10):
    block_x.append(random.randrange(Screen_w - block_w))
    block_y.append(random.randrange(Screen_h - block_h))
    Hit.append(False)

Score = 0

font = pygame.font.Font(None,50)

 

done = False
clock =pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True       
        
    screen.fill(White)
    
    pos = pygame.mouse.get_pos()
    player_x = pos[0]
    player_y = pos[1]
    pygame.draw.rect(screen,RED,[player_x, player_y, player_w, player_h])
    for i in range(10):
        if Hit[i] == False:
           pygame.draw.rect(screen, Black, [block_x[i], block_y[i], block_w, block_h])
    for i in range(10):  
         xin = block_x[i] <= player_x <= block_x[i] + block_w or block_x[i] <= player_x + player_w <=block_x[i] + block_w 
         yin = block_y[i] <= player_y <= block_y[i] + block_h or block_y[i] <= player_y + player_h <=block_y[i] + block_h
         if xin and yin and Hit[i] == False:
             Hit[i] = True
             Score = Score + 1
        
        
    mes = str(Score) + "Points"    
    text = font.render(mes, 10, Black)    
    screen.blit(text, (40,40))    
    
    
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


    
