import sys
import random
import pygame
from pygame.locals import *
import math
from pygame import gfxdraw
from copy import deepcopy
from numba import jit
import numpy as np
#sv = input("Starting Vector: ")
#co = input("cords: ")
from FastLine import Line

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
gcons = 10
#300 150
pygame.display.set_caption('Gravity')
n = 10
o = 0
class Planet():
    def __init__(self,xpos,ypos,vx,vy,mass,radius,move):
        self.xpos = int(xpos)
        self.ypos = int(ypos)
        self.vx = int(vx)
        self.vy = int(vy)
        self.mass = mass
        self.radius = radius
        self.move = move
        self.forces = []

    def drawplanet(self):
        if flag3:
            #print(self.xpos,self.ypos)
            pygame.draw.circle(screen, white, (round(self.xpos), round(self.ypos)), self.radius, 0)





    def __eq__(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return True
        else:
            return False

objects = [Planet(700,450,0,2,500,10,True),Planet(1100,450,0,-2,500,10,True),Planet(900,650,2,0,500,10,True),Planet(900,250,-2,0,500,10,True)]
speed = 5
#objects = [Planet(900,450,0,0,100,10),   Planet(800,450,0,-20,100,10),Planet(1000,450,0,20,100,10),Planet(900,350,20,0,100,10),Planet(900,550,-20,0,100,10),     Planet(600,450,0,-25,100,10),Planet(1200,450,0,25,100,10),Planet(900,150,25,0,100,10),Planet(900,750,-25,0,100,10) ,     Planet(400,450,0,28,100,10),Planet(1400,450,0,-28,100,10),Planet(900,-50,-28,0,100,10),Planet(900,950,28,0,100,10)]
#objects = [Planet(900,450,0,0,35000,10), Planet(600,450,-7,-15,100,10),Planet(1200,450,7,15,100,10),Planet(900,150,15,-7,100,10),Planet(900,750,-15,7,100,10),]
# for x in range(0,width,100):
#     for y in range(0,height,100):
#         objects.append([x,y,0,0,x*100,10])
# x,y , v1x , v1y, mass , radius, hit?
pi = math.pi
def PointsInCircum(r,n=100):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n)]


fpsClock = pygame.time.Clock()
def backg1():
    screen.fill(black)

# tot = PointsInCircum(250,8)
# for count,each in enumerate(tot):
#     objects.append(Planet(each[0]+ 900,each[1]+ 450,0,0,-40,10,True))
# objects.append(Planet(900,450,0,0,300,10,True))
def hitdetect(objs):
    nl = deepcopy(objs)
    for each in objs:
        for every in objs:
            if every != each:
                dist = math.sqrt((every.xpos - each.xpos)**2 + (every.ypos - each.ypos)**2)
                if dist < each.radius + every.radius:
                    print('COLIDE')
                    nx = (each.mass*each.vx + every.mass*every.vx) /(each.mass + every.mass)
                    ny = (each.mass*each.vy + every.mass*every.vy) /(each.mass + every.mass)
                    print(nl)
                    #nl.append(Planet((each.xpos + every.xpos)/2,(each.xpos + every.xpos)/2,nx,ny,each.mass + every.mass,each.radius + every.radius,True))
                    nl.append(Planet((each.xpos + every.xpos)/2,(each.ypos + every.ypos)/2,nx,ny,each.mass + every.mass,int(math.sqrt(each.radius**2 + every.radius**2)),True))

                    nl.remove(each)
                    nl.remove(every)
                    break


    return nl
        #print(gforce,angle)
total = []

pre = []
length = 5

def PointsInCircum(r,n=100):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n)]
# tot = PointsInCircum(100,8)
# for count,each in enumerate(tot):
#     if count%2 != 0:
#         objects.append(Planet(each[0]+ 900,each[1]+ 450,0,0,100,10,True))


def flow(lis):
    step = 10
    for x in range(0,1800,step):
        for y in range(0,900,step):
            totalaccely = 0
            totalaccelx = 0
            angle2 = 0
            for each in lis:

                dirx = int(each.xpos - x)
                diry = int(each.ypos - y)
                if dirx != 0 and diry != 0:
                    gforce = gcons * (each.mass) / ((math.sqrt(abs(dirx)**2+abs(diry)**2))**2)
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

# x,y , v1x , v1y, mass , radius, hit?
point = 5
def mainloop(lis):
    l = lis
    for each in lis:

        if each.xpos < -20 or each.xpos > 1820 or each.ypos < -20 or each.ypos > 920:
            l.remove(each)

    newobjs = deepcopy(l)




    for counter,sel in enumerate(l):
        if sel.move:
            totalfx = 0
            totalfy = 0
            for each in l:

                if each != sel:
                    dirx = int(each.xpos - sel.xpos)
                    diry = int(each.ypos- sel.ypos)
                    if diry!= 0 or dirx != 0:
                        gforce = gcons * (sel.mass*each.mass) / ((math.sqrt(abs(dirx)**2+abs(diry)**2))**2)
                    else:
                        gforce = 0
                    #print(f'Gforce of {counter}: {gforce}')
                    angle = math.degrees(math.atan2(diry,dirx))
                    fy = math.sin(math.radians(angle)) * gforce
                    fx = math.cos(math.radians(angle)) * gforce


                    # if diry < 0:
                    #     accely *= -1
                    # if dirx < 0:
                    #     accelx *= -1
                    totalfx += fx
                    totalfy += fy

            totalaccely = totalfy/sel.mass
            totalaccelx = totalfx / sel.mass

            newobjs[counter].vx += totalaccelx
            newobjs[counter].vy += totalaccely

            newobjs[counter].xpos +=  newobjs[counter].vx
            newobjs[counter].ypos +=  newobjs[counter].vy



    final = deepcopy(newobjs)
    return final


# x,y , v1x , v1y, mass , radius, hit?

counter = 0
flag = False
flag2 = False
flag3= True
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
                objects.append(Planet(x,y,0,10,10000,10,True))
                pre.append([x,y])
            if event.button == 3:
                x,y = xcord,ycord
                objects.append(Planet(x,y,0,-10,10000,10,True))
                pre.append([x,y])
            if event.button == 2:
                x,y = xcord,ycord
                objects.append(Planet(x,y,0,0,500,10,True))
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
            if event.key == pygame.K_b:
                if flag3:
                    flag3 = False
                else:
                    flag3 = True
    if flag:
        if counter % speed == 0:
            first = deepcopy(hitdetect(objects))
            second = deepcopy(mainloop(first))
            objects = deepcopy(second)

        counter += 1
    if flag2:
        flow(objects)
    if len(total) > 2000:
        total.remove(total[0])
    for count,each in enumerate(objects):
        each.drawplanet()
        total.append((each.xpos,each.ypos))
    #objects = hitdetect(objects)
    for counter,each in enumerate(total):
        screen.set_at((int(each[0]), int(each[1])), (255, 255, 255))


    fpsClock.tick(60)
    pygame.display.update()