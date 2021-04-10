# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:00 2021

@author: carols1107
"""

import pygame

Black = (0,0,0)
White = (255,255,255)
     
pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Ship')

clock =pygame.time.Clock()

background_pos = [0,0]

background_ing = pygame.image.load("Saturn.jpg").convert()

player_ing = pygame.image.load("Ship.png").convert()

player_ing.set_colorkey(Black)

click_Sound = pygame.mixer.Sound("laser.ogg")
pygame.mixer.music.load("Background.mp3")
pygame.mixer.music.play()

done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_Sound.play()
        
    screen.blit(background_ing,background_pos)
    player_pos = pygame.mouse.get_pos()
    x = player_pos[0]
    y = player_pos[1]
    
    screen.blit(player_ing,[x - 50,y - 50])
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


    
