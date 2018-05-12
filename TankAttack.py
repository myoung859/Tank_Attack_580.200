# -*- coding: utf-8 -*-
"""
Created on Tue May  1 09:32:34 2018

@author: myoun
"""

import pygame
import helpers as TA


print("Welcome to Tank Attack!")

while(True):
    start = input("To begin, type play. To change parameters type options.")

    if start[-1].lower() == 'p':
        options = False;
        break
        
    if start[-1].lower() == 'o':
        options = True;
        break

filer=open('options.csv', 'r')
x_dim = filer.readline()
y_dim = filer.readline()
gravity = filer.readline()
drag = filer.readline()
filer.close()


if options == True:
    filew = open('options.csv', 'w')
    
    
field = (300, 500)
screen = pygame.display.set_mode(field)

pygame.display.set_caption("Tank Attack")
screen.fill([0,0,255])
pygame.display.flip()


        