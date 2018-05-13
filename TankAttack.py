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

pygame.init()

field = [x_dim, y_dim]
screen = pygame.display.set_mode(field)
pygame.display.set_caption("Tank Attack")

print("Welcome to Tank Attack!")

def hit():
    return False

def sho(p1,p2,bar_p1,bar_p2, x_dim, y_dim):
    pygame.display.set_mode((x_dim,y_dim))
    screen.fill([0,0,255])
    pygame.draw.rect(screen, [139,69,19],[0,y_dim-50,x_dim,500], 0)
    pygame.draw.circle(screen,p1[1],(p1[0]+20,230),10, 0)
    pygame.draw.rect(screen,p1[1],[p1[0],230,40,20], 0)
    screen.blit(bar_p1, (p1[0], 225))
    screen.blit(bar_p2, (p2[0], 225))
    pygame.draw.circle(screen,p2[1],(p2[0] + 20,230),10, 0)
    pygame.draw.rect(screen,p2[1],[p2[0],230,40,20], 0)
    pygame.display.flip()

def shoot(velocity, angle):
    return

def initalized():
    i = int(rd.random()*500)

    if i > 450:
        i = i - 50
    elif i < 50:
        i = i + 50
    return i

p1 = [initalized(), [0,255,0],1]
p2 = [initalized(), [255,0,0],2]
bar_p1 = pygame.image.load('p1_tankbarrel.png')
bar_p2 = pygame.image.load('p2_tankbarrel.png')

#Repeatedly prompts the user until they type 'o' or 'p'
while(True):
    start = input("To begin, type play. To change parameters type options.")

    if start[-1].lower() == 'p':
        p = 1

        while hit() == False:
            sho(p1,p2,bar_p1,bar_p2, x_dim, y_dim)
            print("Player " + str(p))
            print("If you want to move your tank 50 meters back. Press A.")
            print("If you want to fire a shell from your tank, Press B.")
            opt = str(input())

            if (opt[-1].lower() == 'a'):
                options = False;
                # Grab angle and velocity values
                angle = float(input("Enter the angle."))
                velocity = float(input("Enter the velocity."))
                if p == 1:
                    bar_p1 = pygame.transform.rotate(bar_p1, angle)
                elif p == 2:
                    bar_p2 = pygame.transform.rotate(bar_p2, angle)
                shoot(velocity, angle)
            elif (opt[-1].lower() == 'b'):
                dir = input("Move To The Left or Right? Type a letter. (L/R)")
                
                if p == 1:
                    if dir == 'L':
                        p1[0] = p1[0] - 10
                    elif dir == 'R':
                        p1[0] = p1[0] + 10
                        
                elif p == 2:
                    if dir == 'L':
                        p1[0] = p1[0] - 10
                    elif dir == 'R':
                        p2[0] = p2[0] + 10
                        
            sho(p1,p2,bar_p1,bar_p2, x_dim, y_dim)
            if p == 1:
                p = 2
            elif p == 2:
                p = 1
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
