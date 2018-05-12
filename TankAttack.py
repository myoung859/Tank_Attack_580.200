# -*- coding: utf-8 -*-
"""
Created on Tue May  1 09:32:34 2018

@author: myoun
"""

import pygame
import helpers as TA

#Initial parameter setup
filer=open('options.csv', 'r',newline = '')
x_dim = int(filer.readline())
y_dim = int(filer.readline())
gravity = float(filer.readline())
drag = float(filer.readline())
wind_max = float(filer.readline())
filer.close()

print("Welcome to Tank Attack!")


def hit():
    return False

def init():
    i = rd.random()*240
    return i

#Repeatedly prompts the user until they type 'o' or 'p'
while(True):
    start = input("To begin, type play. To change parameters type options.")

    if start[-1].lower() == 'p':
        options = False;
        while hit() == False:
            angle = float(input("Enter the angle."))
            velocity = float(input("Enter the velocity."))
        
        break
        
    if start[-1].lower() == 'o':
        TA.options_prompt('options.csv',x_dim,y_dim,gravity,drag, wind_max)
        filer=open('options.csv', 'r',newline = '')
        x_dim = int(filer.readline())
        y_dim = int(filer.readline())
        gravity = float(filer.readline())
        drag = float(filer.readline())
        wind_max = float(filer.readline())
        filer.close()

        
    
field = [x_dim, y_dim]
screen = pygame.display.set_mode(field)

pygame.display.set_caption("Tank Attack")
#Draw sky and ground
screen.fill([0,0,255])
pygame.draw.rect(screen, [139,69,19],[0,y_dim-50,x_dim,500], 0)
pygame.display.flip()


        
