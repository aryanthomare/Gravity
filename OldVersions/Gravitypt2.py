import sys
import random
import pygame
from pygame.locals import *
import math
from pygame import gfxdraw
from copy import deepcopy
import numpy as np
#sv = input("Starting Vector: ")
#co = input("cords: ")

#co = co.split(" ")
#x= int(co[0])
#y= int(co[1])
x = 200
y = 200
white = (255,255,255)
green = (165,238,93)
pink = (245,212,229)
red = (230,69,83)
blue = (85,75,230)
black = (0,0,0)
grey = (130,130,130)
pygame.init()
width, height = 1800,900
screen = pygame.display.set_mode((width,height))
gcons = 5
#300 150
pygame.display.set_caption('Gravity')
n = 10
o = 0

objects = []

# for x in range(0,width,100):
#     for y in range(0,height,100):
#         objects.append([x,y,0,0,x*100,10])
# x,y , v1x , v1y, mass , radius, hit?



fpsClock = pygame.time.Clock()
def backg1():
    screen.fill(black)

def plyr(x,y,r):
    #pygame.draw.circle(screen, white, (int(x), int(y)), r, 0)
    pass

def hitdetect(objs):
    if len(objs) > 1:
        all = []
        for each in objs:
            for others in objs:
                if others != each:
                    if (each[5] + others[5]) >= math.sqrt((abs(each[0]-others[0])**2 +  abs(each[1]-others[1])**2)):
                        new = deepcopy(each)
                        new[6] = True
                        print('hit')
                        all.append(new)
                    else:
                        all.append(each)
        return all
    else:
        return objs

        #print(gforce,angle)
total = []

pre = []
length = 5

def flow(lis):
    step = 10
    for x in range(0,1800,step):
        for y in range(0,900,step):
            totalaccely = 0
            totalaccelx = 0
            angle2 = 0
            for each in lis:

                dirx = int(each[0] - x)
                diry = int(each[1] - y)
                if dirx != 0 and diry != 0:
                    gforce = gcons * (each[4]) / ((math.sqrt(abs(dirx)**2+abs(diry)**2))**2)
                else:
                    gforce = 0
                #print(f'Gforce of {counter}: {gforce}')

                if dirx == 0:
                    angle = 90
                if diry == 0:
                    angle = 0





                if dirx != 0 and diry != 0:
                    angle = math.degrees(math.atan(diry/dirx))
                accely = abs(math.degrees(math.sin(math.radians(angle))) * gforce)
                accelx = abs(math.degrees(math.cos(math.radians(angle))) * gforce)
                if diry < 0:
                    accely *= -1
                if dirx < 0:
                    accelx *= -1
                totalaccelx += accelx
                totalaccely += accely
            if totalaccelx != 0:

                angle2 = math.degrees(math.atan(totalaccely/totalaccelx))

            pygame.draw.line(screen, white, ( x- math.cos(math.radians(angle2))* length, y - math.sin(math.radians(angle2))*length), (x + math.cos(math.radians(angle2))*length, y + math.sin(math.radians(angle2))*length), 2)

def mainloop(lis):
    newobjs = deepcopy(lis)
    for counter,sel in enumerate(lis):
        totalaccelx = 0
        totalaccely = 0
        for each in lis:

            if each != sel:
                dirx = int(each[0] - sel[0])
                diry = int(each[1] - sel[1])
                gforce = gcons * (sel[4]*each[4]) / ((math.sqrt(abs(dirx)**2+abs(diry)**2))**2)
                #print(f'Gforce of {counter}: {gforce}')

                if dirx == 0:
                    angle = 90
                if diry == 0:
                    angle = 0





                if dirx != 0 and diry != 0:
                    angle = math.degrees(math.atan(diry/dirx))
                accely = abs(math.degrees(math.sin(math.radians(angle))) * gforce)
                accelx = abs(math.degrees(math.cos(math.radians(angle))) * gforce)
                if diry < 0:
                    accely *= -1
                if dirx < 0:
                    accelx *= -1
                totalaccelx += accelx
                totalaccely += accely

        totalaccely = totalaccely/sel[4]
        totalaccelx = totalaccelx / sel[4]

        newobjs[counter][0] += (totalaccelx + newobjs[counter][2])
        newobjs[counter][1] += (totalaccely + newobjs[counter][3])

        newobjs[counter][2] += totalaccelx
        newobjs[counter][3] += totalaccely


    for each in newobjs:
        if each[0] < -20 or each[0] > 1820 or each[1] < -20 or each[1] > 920:
            newobjs.remove(each)
            pass
    final = deepcopy(newobjs)
    return final


# x,y , v1x , v1y, mass , radius, hit?

counter = 0
flag = False
flag2 = False
while True:
    xcord, ycord = pygame.mouse.get_pos()
    backg1()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = xcord,ycord
                objects.append([x,y,0,5,100,10,False])
                pre.append([x,y])
            if event.button == 3:
                x,y = xcord,ycord
                objects.append([x,y,0,-5,100,10,False])
                pre.append([x,y])
            if event.button == 2:
                x,y = xcord,ycord
                objects.append([x,y,0,0,-1000,10,False])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                total = []

            if event.key == pygame.K_f:
                if flag2:
                    flag2 = False
                else:
                    flag2 = True
            if event.key == pygame.K_SPACE:
                if flag:
                    flag = False
                else:
                    flag = True

    if flag:
        if counter % 1 == 0:

            objects = mainloop(objects)
        counter += 1
    if flag2:
        flow(objects)

    for count,each in enumerate(objects):
        plyr(each[0],each[1],each[5])
        total.append((each[0],each[1],count))
    #objects = hitdetect(objects)
    c = 0
    for each in total:
        gfxdraw.pixel(screen, int(each[0]), int(each[1]),(255,255,255))
        c += 1


    fpsClock.tick(60)
    pygame.display.update()