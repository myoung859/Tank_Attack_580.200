# -*- coding: utf-8 -*-
"""
Created on Tue May  1 09:32:34 2018

@author: myoun
"""

import pygame
import random as rd
import helpers as TA

#Initial parameter setup
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


print("Welcome to Tank Attack!")

def playertank(p, angle):
    if p == 1:
        bar = pygame.image.load('p1_tankbarrel.png')
    elif p ==2:
        bar = pygame.image.load('p2_tankbarrel.png')

    pygame.transform.rotate(bar, angle)
    return

def hit():
    return False

def init():
    i = int(rd.random()*190)
    return i

p1 = [init(), [0,255,0],1]
p2 = [init() + 200, [255,0,0],2]

#Repeatedly prompts the user until they type 'o' or 'p'
while(True):
    start = input("To begin, type play. To change parameters type options.")

    if start[-1].lower() == 'p':
        p = 1
        print("Player " + str(p))
        print("If you want to move your tank 50 meters back. Press A.")
        print("If you want to fire a shell from your tank,")
        opt = str(input())

        if (opt[-1].lower() == 'a'):
            options = False;
            # Grab angle and velocity values
            angle = float(input("Enter the angle."))
            velocity = float(input("Enter the velocity."))
            playertank(p, angle)
        elif (opt[-1].lower() == 'b'):
            if p == 1:
                p1[0] = p1[0] + 50
            elif p == 2:
                p2[0] = p2[0] - 50

        if p == 1:
            p = 2
        elif p == 2:
            p = 1

        screen.fill([0,0,255])
        pygame.draw.rect(screen, [139,69,19],[0,y_dim-50,x_dim,500], 0)
        pygame.draw.circle(screen,p1[1],(p1[0]+20,230),10, 0)
        pygame.draw.rect(screen,p1[1],[p1[0],230,40,20], 0)
        pygame.draw.circle(screen,p2[1],(p2[0] + 20,230),10, 0)
        pygame.draw.rect(screen,p2[1],[p2[0],230,40,20], 0)
        pygame.display.flip()
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
