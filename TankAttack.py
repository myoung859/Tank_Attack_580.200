import pygame
import random as rd
from helpers import Tank
from helpers import Shell
import helpers as TA

#Initial parameter setup
filer=open('options.csv', 'r',newline = '')
x_dim = 500
y_dim = 500
gravity = 9.8
drag = 5
wind_max = 10
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
    start = input("To begin, type (P)lay. To change parameters type (O)ptions.")

	if start[0].lower() == 'o':
        TA.options_prompt('options.csv',x_dim,y_dim,gravity,drag, wind_max)
        filer=open('options.csv', 'r',newline = '')
        x_dim = int(filer.readline())
        y_dim = int(filer.readline())
        gravity = float(filer.readline())
        drag = float(filer.readline())
        wind_max = float(filer.readline())
        filer.close()


    if start[0].lower() == 'p':
        field = [x_dim, y_dim]
        ip1 = initalized(x_dim)
        ip2 = initalized(x_dim)

        p1 = Tank(ip1, x_dim, y_dim, 1, 'p1tank.png')
        p2 = Tank(ip2, x_dim, y_dim, 2, 'p2tank.png')
        
        pygame.init()
        b=rd.random()
        windy=b*wind_max
        
        p = 1
        screen = pygame.display.set_mode(field)
        show(p1,p2, screen)
        pygame.display.flip()
        col = False
        
        a=rd.random()
        b=rd.random()
        windy=b*wind_max
        if a<0.5:
            v_wind=windy
            print('The wind is blowing %.2f mph to the right.'%windy)
        else:
            v_wind=windy*-1
            print('The wind is blowing %.2f mph to the left.'%windy)
        
        while col == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    break
            screen = pygame.display.set_mode(field)
            show(p1,p2, screen)
            pygame.display.flip()
            
	    	opt = 'IFYOUREADTHISGIVEUSANA'
            while (not (opt[0].lower() in ['f','m','q'])):
                print("If you want to fire a shell from your tank, input (F)ire.")
                print("If you want to move your tank up to 50 meters, input (M)ove.")
                print("To quit, input (Q)uit")
                opt = str(input())

            if start.lower() == 'q':
                pygame.display.quit()
                pygame.quit()
                break

            if (opt[0].lower() == 'f'):
                v_0 = float(input("Input the initial velocity: "))
                angle = float(input("Input the angle of your shot (degrees): "))
                pygame.display.flip()
                if p == 1:
                    shot = Shell(v_0, angle, p1)
                    while shot.y_pos > 0 and shot.x_pos > 0 and shot.y_pos > -1*(y_dim-50) and shot.x_pos < shot.Tank.x_max and col==False:
                        shot.Fire(drag, v_wind, gravity, 0.5)
                        yposition = shot.y_pos
                        if shot.y_pos < 0:
                            yposition = shot.y_pos*-1
                        screen = pygame.display.set_mode(field)
                        show(p1,p2, screen)
                        fire = pygame.draw.rect(screen,shot.color,[shot.x_pos,yposition,10,10],0)
                        col = pygame.Rect.colliderect(fire, p2.rect)
                        if col == True:
                            screen.blit(pygame.image.load('dead.png'), (p2.position(),y_dim-85))
                        pygame.display.flip()

                elif p == 2:
                    shot = Shell(v_0, angle, p2)
                    col = False
                    while shot.y_pos > 0 and shot.x_pos > 0 and shot.y_pos > -1*(y_dim-50) and shot.x_pos < shot.Tank.x_max and col==False:
                        shot.Fire(drag, v_wind, gravity, 0.5)
                        yposition = shot.y_pos
                        if shot.y_pos < 0:
                            yposition = shot.y_pos*-1
                        screen = pygame.display.set_mode(field)
                        show(p1,p2, screen)
                        fire = pygame.draw.rect(screen,shot.color,[shot.x_pos,yposition,10,10],0)
                        col = pygame.Rect.colliderect(fire, p1.rect)
                        if col == True:
                            screen.blit(pygame.image.load('dead.png'), (p1.position(),y_dim-85))
                        pygame.display.flip()

                if col == True:
                    print("Congratulations, Player " + str(p) +".")
                    print("You totally annihilated the other player.")
                    break

            elif (opt[0].lower() == 'm'):
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



    if start.lower() == 'q':
        pygame.quit
        break
