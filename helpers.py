# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:17:05 2018

@author: myoun
"""
import csv

def options_prompt(filename, x_dim, y_dim, gravity, drag):

    filew = open(filename, 'w',newline = '')
    output = csv.writer(filew)
    output.writerow([int(input("Please input the horizontal window size (Current value is "+ str(x_dim) +"): "))])
    output.writerow([int(input("Please input the vertical window size (Current value is "+ str(y_dim) +"): "))])
    output.writerow([float(input("Please input the gravity strength (Current value is "+ str(gravity) +"): "))])
    output.writerow([float(input("Please input the drag coefficient (Current value is "+ str(drag) +"): "))])
