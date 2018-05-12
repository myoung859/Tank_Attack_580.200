# -*- coding: utf-8 -*-
"""
Created on Tue May  1 09:32:34 2018

@author: myoun
"""

import pygame
import helpers as TA

#Initial parameter setup
filer=open('options.csv', 'r',newline = '')
x_dim = filer.readline()
print(x_dim)
y_dim = filer.readline()
gravity = filer.readline()
drag = filer.readline()
filer.close()

print("Welcome to Tank Attack!")

#Repeatedly prompts the user until they type 'o' or 'p'
while(True):
    start = input("To begin, type play. To change parameters type options.")

    if start[-1].lower() == 'p':
        options = False;
        break
        
    if start[-1].lower() == 'o':
        TA.options_prompt('options.csv',x_dim,y_dim,gravity,drag)
        filer=open('options.csv', 'r',newline = '')
        x_dim = filer.readline()
        print(x_dim)
        y_dim = filer.readline()
        gravity = filer.readline()
        drag = filer.readline()
        filer.close()

        

if options == True:
    TA.options_prompt('options.csv',x_dim,y_dim,gravity,drag)
    
field = (300, 500)
screen = pygame.display.set_mode(field)

pygame.display.set_caption("Tank Attack")
screen.fill([0,0,255])
pygame.display.flip()


        