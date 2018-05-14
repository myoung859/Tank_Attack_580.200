import pygame
import random as rd
from helpers import Tank

#Initial parameter setup
filer=open('options.csv', 'r',newline = '')
x_dim = 500
y_dim = 500
gravity = float(filer.readline())
drag = float(filer.readline())
wind_max = float(filer.readline())
filer.close()

pygame.init()
field = [x_dim, y_dim]

pygame.display.set_caption("Tank Attack")

print("Welcome to Tank Attack!")

def show(p1, p2):
    screen = pygame.display.set_mode(field)
    screen.fill([0,0,156])
    pygame.draw.rect(screen, [0,56,0],(0,y_dim-50,x_dim,y_dim),0)
    screen.blit(p1.showtank(), (p1.position(),y_dim-85))
    screen.blit(p2.showtank(), (p2.position(),y_dim-85))
    pygame.display.flip()
    return

def hit():
    return False

def initalized(x_dim):
    i = int(rd.random()*x_dim)

    if i > (x_dim - 50):
        i = i - 50
    elif i < 50:
        i = i + 50
    return i

def fire():
    return

ip1 = initalized(x_dim)
ip2 = initalized(x_dim)

p1 = Tank(ip1, x_dim, y_dim, 1, 'p1tank.png')
p2 = Tank(ip2, x_dim, y_dim, 2, 'p2tank.png')

#Repeatedly prompts the user until they type 'o' or 'p'
while(True):
    show(p1,p2)
    start = input("To begin, type P. To change parameters type O.")

    if start[-1].lower() == 'p':
        p = 1

        while hit() == False:
            print("Player " + str(p))
            print("If you want to fire a shell from your tank, press F.")
            print("If you want to move your tank 50 meters back, press M.")
            opt = str(input())

            if (opt[-1].lower() == 'f'):
                fire()
                hit()
            elif (opt[-1].lower() == 'm'):
                if p == 1:
                    p1.move()
                elif p == 2:
                    p2.move()

            show(p1,p2)
            if p == 1:
                p = 2
            elif p == 2:
                p = 1

        if hit() == True:
            print("Congratulations, Player " + str(p) +".")
            print("You totally annihilated the other player.")

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
