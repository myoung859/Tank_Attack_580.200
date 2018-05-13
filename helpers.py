# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:17:05 2018

@author: myoun
"""
import csv
import pygame

def options_prompt(filename, x_dim, y_dim, gravity, drag,wind_max):

    filew = open(filename, 'w',newline = '')
    output = csv.writer(filew)
    output.writerow([int(input("Please input the horizontal window size (Current value is "+ str(x_dim) +"): "))])
    output.writerow([int(input("Please input the vertical window size (Current value is "+ str(y_dim) +"): "))])
    output.writerow([float(input("Please input the gravity strength (Current value is "+ str(gravity) +"): "))])
    output.writerow([float(input("Please input the drag constant (Current value is "+ str(drag) +"): "))])
    output.writerow([float(input("Please input the maximum wind speec (Current value is "+ str(drag) +"): "))])

class Tank(pygame.sprite.Sprite):
    def __init__(self, pos_x, x_dim, y_dim, color, player):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((25, 13))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, y_dim-63)
        self.player = player
        self.x_max = x_dim
    def move(self):
        dist = 666 #Hail santa!
        while (dist > 50 or dist <= -50):
            dist = int(input("Please enter the distance (positive or negative) to move, up to 50 meters: "))
        self.rect.left = self.rect.x + (5* dist) #Inspired by https://bit.ly/2KkNOp8
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > self.x_max):
            self.rect.right = self.x_max
            
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
    