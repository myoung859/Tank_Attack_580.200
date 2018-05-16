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
    output.writerow([float(input("Please input the maximum wind speed (Current value is "+ str(wind_max) +"): "))])

class Tank(pygame.sprite.Sprite):
    def __init__(self, pos_x, x_dim, y_dim, player, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.ymax = y_dim
        self.positx= pos_x
        self.rect.center = (self.positx + 15, y_dim-63) #bottom of tank is on ground
        self.posx = pos_x+15
        if player == 1:
            self.color = [255,0,0]
        elif player == 2:
            self.color = [0,255,0]           
        self.posy = y_dim-63
        self.player = player
        self.x_max = x_dim
        
    def move(self):
        dist = 516
        while (dist > 50 or dist < -50):
            dist = int(input("Please enter the distance (positive-RIGHT or negative-LEFT) to move, up to 50 meters: "))
        self.positx = self.positx + int(2.5*dist) #Inspired by https://bit.ly/2KkNOp8
        if (self.positx <= 20):
            self.positx = 0
            print("You can't get out of this one.")
        if (self.positx >= self.x_max - 20):
            self.positx = self.x_max
            print("You can't get out of this one.")
        return self.positx

    def showtank(self):
       pic = self.image
       return pic         

    def position(self):
        return self.positx

    def color(self):
        return self.color
    
    def fire(self):
        None
class Shell(pygame.sprite.Sprite):
    def __init__(self, v_0, angle, Tank):
        super().__init__()
        self.image = pygame.image.load('bullet.png')
        self.color = [255,0,255]
        self.rect = self.image.get_rect()
        self.Tank = Tank
        self.rect.center = (self.Tank.rect.centerx, self.Tank.rect.centery - 6)        
        self.player = getattr(self.Tank, 'player')
        self.v_x = cos(radians(angle)) * v_0
        self.v_y = sin(radians(angle)) * v_0
        self.mass = 10
        self.x_pos=self.Tank.posx
        self.y_pos=self.Tank.posy
        
    def Fire(self,drag,v_wind, gravity,dt):
        #Calculates real-time change in velocity, then moves the shell that much
        self.v_x = self.v_x - ((drag*(self.v_x + v_wind)/self.mass)*dt)
        self.v_y = self.v_y - ((drag*(self.v_y)/self.mass)*dt) - (gravity * dt)
        self.x_pos=self.x_pos+dt*self.v_x
        self.y_pos=self.y_pos-dt*self.v_y
        
