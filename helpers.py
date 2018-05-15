# -*- coding: utf-8 -*-
"""
Created on Sun May 13 17:35:38 2018

@author: Mike
"""
import pygame
from math import radians,sin,cos
import csv
import random

def options_prompt(filename, x_dim, y_dim, gravity, drag,wind_max):

    filew = open(filename, 'w',newline = '')
    output = csv.writer(filew)
    output.writerow([int(input("Please input the horizontal window size (Current value is "+ str(x_dim) +"): "))])
    output.writerow([int(input("Please input the vertical window size (Current value is "+ str(y_dim) +"): "))])
    output.writerow([float(input("Please input the gravity strength (Current value is "+ str(gravity) +"): "))])
    output.writerow([float(input("Please input the drag constant (Current value is "+ str(drag) +"): "))])
    output.writerow([float(input("Please input the maximum wind speec (Current value is "+ str(drag) +"): "))])

class Tank(pygame.sprite.Sprite):
    def __init__(self, pos_x, x_dim, y_dim, player, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, y_dim-63)
        self.posx = pos_x
        self.player = player
        self.x_max = x_dim
    def move(self):
        dist = 516
        while (dist > 50 or dist <= -50):
            dist = int(input("Please enter the distance (positive-RIGHT or negative-LEFT) to move, up to 50 meters: "))
        self.posx = self.posx + int(2.5*dist) #Inspired by https://bit.ly/2KkNOp8
        if (self.posx <= 20):
            self.posx = 0
            print("You can't get out of this one.")
        if (self.posx >= self.x_max - 20):
            self.posx = self.x_max
            print("You can't get out of this one.")
        return self.posx

    def showtank(self):
       pic = self.image
       return pic         

    def position(self):
        return self.posx

    def color(self):
        return self.color
    
    def fire(self):
        None
class Turret(pygame.sprite.Sprite):
    def __init__(self, associated): #link with body
        super().__init__()
        self.associated = associated
        self.player = getattr(self.associated, 'player')
        self.image = pygame.Surface([24,24])
        pygame.draw.circle(self.image, getattr(self.associated, 'color'), (12, 12),6)
        self.rect = self.image.get_rect()
        self.rect.center = (self.associated.rect.centerx, self.associated.rect.centery - 6)
        self.image.set_colorkey([0,0,0])
    def update(self):
        self.rect.x = self.associated.rect.x
class Shell(pygame.sprite.Sprite):
    def __init__(self, v_0, angle, Tank):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill([0, 255, 0])
        self.rect = self.image.get_rect()
        self.Tank = Tank
        self.rect.center = (self.Tank.rect.centerx, self.Tank.rect.centery - 6)        
        self.player = getattr(self.Tank, 'player')
        self.v_x = cos(radians(angle)) * v_0
        self.v_y = sin(radians(angle)) * v_0
        self.mass = 10
        a=random.random()
        b=random.random()
        windy=b*wind_max
        if a<0.5:
            v_wind=windy
            print('The wind is blowing '+str(windy)+'mph to the right.')
        else:
            v_wind=windy*-1
            print('The wind is blowing '+str(windy)+'mph to the left.')
        
    def Fire(self,drag,v_wind, gravity,dt):
        #Calculates real-time change in velocity, then moves the shell that much
        self.v_x = self.v_x - ((drag*(self.v_x + v_wind)/self.mass)*dt)
        self.v_x = self.v_x - ((drag*(self.v_y)/self.mass)*dt) - (gravity * dt)
        dx = int((self.v_x * dt*2.5))
        dy = int((self.v_y * dt*2.5))
        print(dx)
        print(dy)
        return self.rect.move(dx,dy)
    
