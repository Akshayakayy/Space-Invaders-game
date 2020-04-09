#################  IMPORTING MODULES  ##################
import pygame
from mod.spaceship import *
from mod.missiles import *
from mod.aliens import *
import random

##################  INITIALIZING PYGAME  ##################
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Space Invader')
clock = pygame.time.Clock()

##################  LOADING IMAGES  #####################
shipimg = pygame.image.load('images/ship2.png')
alien1img = pygame.image.load('images/alien22.png')
alien2img = pygame.image.load('images/alien111.png')
bg = pygame.image.load('images/space.png')

##################  INITIALIZING VARIABLES  ###################
crashed = False
aliens_list = []
missiles_list = []
score = 0
myfont = pygame.font.SysFont('ariel', 40)
count_time = 0

###################  SETTING THE START  #####################
screen.blit(bg,(0,0))

ship_obj = spaceship(206.25,485,shipimg)
ship_obj.draw_ship(screen)

alien_obj = aliens(68.75*random.randint(0,7),2.2+69.4*random.randint(0,1),alien1img,1)
aliens_list.append(alien_obj)

for alien in aliens_list:
    alien.spawn(screen)

###################  THE GAME STARTS  ####################
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #When key is pressed
        if event.type == pygame.KEYDOWN:
            #move spaceship left
            if event.unicode == 'a' or event.unicode == 'A':
                if ship_obj.x-68.75 >= 0:
                    ship_obj.x = ship_obj.x-68.75
            #move spaceship right
            elif event.unicode == 'd' or event.unicode == 'D':
                if ship_obj.x+68.75 <= 500:
                    ship_obj.x = ship_obj.x+68.75
            #launch missile 1
            elif event.unicode == ' ':
                obj_m1 = m1(ship_obj.x,ship_obj.y+3,"m1")
                missiles_list.append(obj_m1)
            #launch missile 2
            elif (event.unicode == 's' or event.unicode == 'S'):
                obj_m2 = m2(ship_obj.x,ship_obj.y+3,"m2")
                missiles_list.append(obj_m2)
            #quit game
            elif event.unicode == 'q' or event.unicode == 'Q':
                pygame.quit()
                quit()

        if ship_obj.x > 500 or ship_obj.x < 0:
            crash()

    #Refreshing
    screen.blit(bg,(0,0))

    #Updating missile position
    for missile in missiles_list:
        if missile.y < 0:
            missiles_list.remove(missile)
        else:
            missile.bullet(screen)
            if missile.type == "m1":
                missile.y -= 69.4/60
            elif missile.type == "m2":
                missile.y -= 69.4/30

    #Adding alien every 10secs
    count_time += 1/600
    if count_time > 1:
        count_time = 0
        alien_obj = aliens(68.75*random.randint(0,7),2.2+69.4*random.randint(0,1),alien1img,1)
        aliens_list.append(alien_obj)

    #Spawning aliens
    for alien in aliens_list:
        if alien.alien_count <= 120/600:
            aliens_list.remove(alien)
        else:
            alien.alien_count -= 1/600
            alien.spawn(screen)

    #Checking for collisions
    for missile in missiles_list:
        for alien in aliens_list:
            if missile.x == alien.x and missile.y < alien.y+39 and missile.y > alien.y+36:
                missiles_list.remove(missile)
                if missile.type == "m1":
                    aliens_list.remove(alien)
                    score += 1
                elif missile.type == "m2":
                    alien.img = alien2img
                    alien.spawn(screen)
                    alien.alien_count += 1/2

    ##  PRINTING THE SCORE  ##
    textsurface = myfont.render('Score: ' + str(score), False, (255, 255, 255))
    screen.blit(textsurface,(242,275))

    ship_obj.draw_ship(screen)
    pygame.display.update()

    clock.tick(60)

###############  GAME ENDS #################
pygame.quit()
quit()
