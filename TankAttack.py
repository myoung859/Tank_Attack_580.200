import pygame
import random as rd
from helpers import Tank
from helpers import Shell
from helpers import Turret
from helpers import Barrel
import helpers as TA

#Initial parameter setup
filer=open('options.csv', 'r',newline = '')
x_dim = 500
y_dim = 500
gravity = 10
drag = 2
wind_max = float(filer.readline())
filer.close()

pygame.init()

pygame.display.set_caption("Tank Attack")

print("Welcome to Tank Attack!")

def show(p1, p2, screen):
    screen.fill([0,0,156])
    Font = pygame.font.SysFont(None, 14)
    pygame.draw.rect(screen, [0,56,0],(0,y_dim-50,x_dim,y_dim),0)
    screen.blit(p1.showtank(), (p1.position(),y_dim-85))
    text = Font.render('P1', True, (255, 0, 0), None)
    screen.blit(text, (p1.position()+15,y_dim-50))
    text2 = Font.render('P2', True, (0, 255, 0), None)
    screen.blit(p2.showtank(), (p2.position(),y_dim-85))
    screen.blit(text2, (p2.position()+15,y_dim-50))
    return

def initalized(x_dim):
    i = int(rd.random()*x_dim)

    if i > (x_dim - 50):
        i = i - 50
    elif i < 50:
        i = i + 50
    return i


#Repeatedly prompts the user until they type 'o' or 'p'
while(True):
    start = input("To begin, type P. To change parameters type O.")

    if start[-1].lower() == 'p':
        field = [x_dim, y_dim]
        ip1 = initalized(x_dim)
        ip2 = initalized(x_dim)

        p1 = Tank(ip1, x_dim, y_dim, 1, 'p1tank.png')
        p2 = Tank(ip2, x_dim, y_dim, 2, 'p2tank.png')
        turp1 = Turret(p1)
        turp2 = Turret(p2)
        
        pygame.init()
        b=rd.random()
        windy=b*wind_max
        
        p = 1
        screen = pygame.display.set_mode(field)
        show(p1,p2, screen)
        pygame.display.flip()
        hit = False
        
        a=rd.random()
        b=rd.random()
        windy=b*wind_max
        if a<0.5:
            v_wind=windy
            print('The wind is blowing %.2f mph to the right.'%windy)
        else:
            v_wind=windy*-1
            print('The wind is blowing %.2f mph to the left.'%windy)
        
        while hit == False:
            screen = pygame.display.set_mode(field)
            show(p1,p2, screen)
            pygame.display.flip()
            print("Player " + str(p))
            print("If you want to fire a shell from your tank, Press F.")
            print("If you want to move your tank 50 meters back. Press M.")
            opt = str(input())

            if (opt[-1].lower() == 'f'):
                v_0 = float(input("Input the initial velocity: "))
                angle = float(input("Input the angle of your shot (degrees): "))
                pt_P1 = (p1.position(), y_dim-85)
                pt_P2 = (p2.position(), y_dim-85)
                pygame.display.flip()
                if p == 1:
                    shot = Shell(v_0, angle, p1)
                    col = False
                    while shot.y_pos > 0 and shot.x_pos > 0 and shot.x_pos < shot.Tank.x_max and col==False:
                        shot.Fire(drag, v_wind, gravity, 1)
                        screen = pygame.display.set_mode(field)
                        show(p1,p2, screen)
                        pygame.draw.rect(screen,[255,255,255],shot,0)
                        pygame.display.flip()
                        col = pygame.sprite.collide_rect(shot, p2)
                elif p == 2:
                    shot = Shell(v_0, angle, p2)
                    col = False
                    while shot.y_pos > 0 and shot.x_pos > 0 and shot.x_pos < shot.Tank.x_max and col==False:
                        shot.Fire(drag, v_wind, gravity, 1)
                        screen = pygame.display.set_mode(field)
                        show(p1,p2, screen)
                        pygame.draw.rect(screen,[255,255,255],shot,0)
                        pygame.display.flip()
                        col = pygame.sprite.collide_rect(shot, p1)

            elif (opt[-1].lower() == 'm'):
                if p == 1:
                    p1.move()
                elif p == 2:
                    p2.move()

                screen = pygame.display.set_mode(field)
                show(p1,p2, screen)
                pygame.display.flip()
            if p == 1:
                p = 2
            elif p == 2:
                p = 1
                a=rd.random()
                b=rd.random()
                windy=b*wind_max
                if a<0.5:
                   v_wind=windy
                   print('The wind is blowing %.2f mph to the right.'%windy)
                else:
                   v_wind=windy*-1
                   print('The wind is blowing %.2f mph to the left.'%windy)

        if hit == True:
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
