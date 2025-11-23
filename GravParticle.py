import sys
import random
import pygame
from pygame.locals import *
import math
from pygame import gfxdraw
from copy import deepcopy
import numpy as np


x = 200
y = 200

white = (255, 255, 255)
green = (165, 238, 93)
pink = (245, 212, 229)
red = (230, 69, 83)
blue = (85, 75, 230)
black = (0, 0, 0)
grey = (130, 130, 130)
pygame.init()
width, height = 1800, 900
screen = pygame.display.set_mode((width, height))
gcons = 1000
# 300 150
pygame.display.set_caption('Gravity')
n = 10
o = 0


class Particle():
    def __init__(self, xpos, ypos, vx, vy, radius):
        self.xpos = int(xpos)
        self.ypos = int(ypos)
        self.vx = int(vx)
        self.mass = 1
        self.vy = int(vy)
        self.radius = radius
        self.hist = []
        self.forcesx = []
        self.forcesy = []
    def drawparticle(self):
        pygame.draw.circle(screen, white, (int(self.xpos), int(self.ypos)), int(self.radius), 0)



    def moveplanet(self):
        self.fx = sum(self.forcesx)
        self.fy = sum(self.forcesy)
        self.accelx = self.fx / self.mass
        self.accely = self.fy / self.mass
        self.vx += self.accelx
        self.vy += self.accely
        self.xpos += self.vx
        self.ypos += self.vy

class Planet():
    def __init__(self, xpos, ypos, vx, vy, mass, radius):
        self.xpos = int(xpos)
        self.ypos = int(ypos)
        self.vx = int(vx)
        self.vy = int(vy)
        self.mass = mass
        self.radius = radius

    def drawplanet(self):
        if flag3:
            pygame.draw.circle(screen, white, (self.xpos, self.ypos), self.radius, 0)

    def __eq__(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return True
        else:
            return False

import math
pi = math.pi
objects = []
# def PointsInCircum(r,n=100):
#     return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n)]
# tot = PointsInCircum(200,20)
# for count,each in enumerate(tot):
#     objects.append(Planet(each[0]+ 900,each[1]+ 450,0,0,-100,10))
# tot = PointsInCircum(400,20)
# for count,each in enumerate(tot):
#     objects.append(Planet(each[0]+ 900,each[1]+ 450,0,0,-100,10))

# tot = PointsInCircum(100,16)
# for count,each in enumerate(tot):
#     objects.append(Planet(each[0]+ 900,each[1]+ 450,0,0,-20,10))
#
#

# tot = PointsInCircum(250,32)
# for count,each in enumerate(tot):
#     objects.append(Planet(each[0]+ 900,each[1]+ 450,0,0,-40,10))
# print(len(objects))
#print(PointsInCircum(10))

speed = 5
#objects = [Planet(700,450,0,0,500,10),Planet(1100,450,0,0,500,10),Planet(900,450,0,0,-700,10)]
# objects = [Planet(900,450,0,0,100,10),   Planet(800,450,0,-20,100,10),Planet(1000,450,0,20,100,10),Planet(900,350,20,0,100,10),Planet(900,550,-20,0,100,10),     Planet(600,450,0,-25,100,10),Planet(1200,450,0,25,100,10),Planet(900,150,25,0,100,10),Planet(900,750,-25,0,100,10) ,     Planet(400,450,0,28,100,10),Planet(1400,450,0,-28,100,10),Planet(900,-50,-28,0,100,10),Planet(900,950,28,0,100,10)]
#objects = [Planet(900,250,0,0,2000,10),Planet(900,650,0,0,2000,10),Planet(900,450,0,0,-3000,10),Planet(700,450,0,0,2000,10),Planet(1100,450,0,0,2000,10)]
#objects = [Planet(0, 900, 0, 0, 500, 10),Planet(0, 0, 0, 0, 500, 10),Planet(1800, 900, 0, 0, 500, 10),Planet(1800, 0, 0, 0, 500, 10),Planet(900, 0, 0, 0, 500, 10),Planet(900, 900, 0, 0, 500, 10)]
# for x in range(0,width,100):
#     for y in range(0,height,100):
#         objects.append([x,y,0,0,x*100,10])
# x,y , v1x , v1y, mass , radius, hit?




fpsClock = pygame.time.Clock()


def backg1():
    screen.fill(black)


particles = []
init = 1000
# for x in range(init):
#     # particles.append(Particle(random.randint(0, 1800), random.randint(0, 900), 0, 0, random.randint(1, 2)))
#
#     particles.append(
#         Particle(random.randint(0, 1800), random.randint(0, 900), 0, 0,
#                  random.randint(1, 2)))


# for x in range(0,1800,30):
#     for y in range(0,900,30):
#         particles.append(Particle(x, y, 0, 0, 1))



def checkparticle(particleslist):
    particlenew = deepcopy(particleslist)
    for each in particlenew:
        if 0 < each.xpos < 1800 or 0 < each.ypos < 900:
            pass
        else:
            particlenew.remove(each)
    if len(particlenew) < init:
        while len(particlenew) < init:
            particlenew.append(
                Particle(random.randint(0, 1800), random.randint(0, 900), 0, 0,
                         random.randint(1, 2)))

    return particlenew
    # newp = Particle(random.randint(0, 1800), random.randint(0, 900), 0, 0, random.randint(1, 2))
    # particles.append(newp)
    # print(newp.xpos,newp.ypos)

    # print(gforce,angle)


total = []

pre = []
length = 5


def flow(lis):
    step = 10
    for x in range(0, 1800, step):
        for y in range(0, 900, step):
            totalaccely = 0
            totalaccelx = 0
            angle2 = 0
            for each in lis:

                dirx = int(each.xpos - x)
                diry = int(each.ypos - y)
                if diry != 0 or dirx != 0:
                    gforce = gcons * (1 * each.mass) / ((math.sqrt(abs(dirx) ** 2 + abs(diry) ** 2)) ** 2)
                else:
                    gforce = random.randint(-1, 1)
                # print(f'Gforce of {counter}: {gforce}')

                angle = math.degrees(math.atan2(diry, dirx))
                accely = math.sin(math.radians(angle)) * gforce
                accelx = math.cos(math.radians(angle)) * gforce

                totalaccelx += accelx
                totalaccely += accely


            if totalaccelx != 0:
                angle2 = math.degrees(math.atan(totalaccely / totalaccelx))

            pygame.draw.line(screen, white,
                             (x - math.cos(math.radians(angle2)) * length, y - math.sin(math.radians(angle2)) * length),
                             (x + math.cos(math.radians(angle2)) * length, y + math.sin(math.radians(angle2)) * length),
                             2)


# x,y , v1x , v1y, mass , radius, hit?
def particleloop(lis, objects):
    newobjs = deepcopy(lis)

    for counter, sel in enumerate(lis):
        totalaccelx = 0
        totalaccely = 0
        for each in objects:

            dirx = int(each.xpos - sel.xpos)
            diry = int(each.ypos - sel.ypos)
            if diry != 0 or dirx != 0:
                gforce = gcons * (sel.mass * each.mass) / ((math.sqrt(abs(dirx) ** 2 + abs(diry) ** 2)) ** 2)
            else:
                gforce = random.randint(-1, 1)
            # print(f'Gforce of {counter}: {gforce}')



            angle = math.degrees(math.atan2(diry, dirx))
            accely = math.sin(math.radians(angle)) * gforce
            accelx = math.cos(math.radians(angle)) * gforce

            totalaccelx += accelx
            totalaccely += accely

        totalaccely = totalaccely / sel.mass
        totalaccelx = totalaccelx / sel.mass

        newobjs[counter].xpos += (totalaccelx + newobjs[counter].vx)
        newobjs[counter].ypos += (totalaccely + newobjs[counter].vy)

        newobjs[counter].vx += totalaccelx
        newobjs[counter].vy += totalaccely

    for each in newobjs:
        if each.xpos < -20 or each.xpos > 1820 or each.ypos < -20 or each.ypos > 920:
            newobjs.remove(each)

    final = deepcopy(newobjs)
    return final

def mainloop(lis):
    newobjs = deepcopy(lis)
    for counter,sel in enumerate(lis):
        totalaccelx = 0
        totalaccely = 0
        for each in lis:

            if each != sel:
                dirx = int(each.xpos - sel.xpos)
                diry = int(each.ypos- sel.ypos)

                gforce = gcons * (sel.mass*each.mass) / ((math.sqrt(abs(dirx)**2+abs(diry)**2))**2)
                #print(f'Gforce of {counter}: {gforce}')


                angle = math.degrees(math.atan2(diry,dirx))
                accely = math.sin(math.radians(angle)) * gforce
                accelx = math.cos(math.radians(angle)) * gforce


                totalaccelx += accelx
                totalaccely += accely

        totalaccely = totalaccely/sel.mass
        totalaccelx = totalaccelx / sel.mass

        newobjs[counter].xpos += (totalaccelx + newobjs[counter].vx)
        newobjs[counter].ypos += (totalaccely + newobjs[counter].vy)

        newobjs[counter].vx += totalaccelx
        newobjs[counter].vy += totalaccely


    for each in newobjs:
        if each.xpos < -20 or each.xpos > 1820 or each.ypos < -20 or each.ypos > 920:
            #newobjs.remove(each)
            pass
    final = deepcopy(newobjs)
    return final


# x,y , v1x , v1y, mass , radius, hit?
rad = 20
counter = 0
flag = False
flag2 = False
flag3 = True
while True:
    xcord, ycord = pygame.mouse.get_pos()
    if flag:
        if len(particles) < init:
            while len(particles) < init:
                # random.randint(xcord-10, xcord+10), random.randint(ycord-10, ycord+10)
                particles.append(
                    Particle(random.randint(xcord-rad, xcord+rad), random.randint(ycord-rad, ycord+rad), 0,0,
                             random.randint(1, 2)))
                # particles.append(
                #     Particle(xcord, ycord, 0, 0,
                #              random.randint(1, 2)))
    backg1()
    #particles = checkparticle(particles)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = xcord, ycord
                objects.append(Planet(x, y, 0, 5, 500, 10))
                pre.append([x, y])
            if event.button == 3:
                x, y = xcord, ycord
                objects.append(Planet(x, y, 0, -5, 500, 10))
                pre.append([x, y])
            if event.button == 2:
                x, y = xcord, ycord
                objects.append(Planet(x, y, 0, 0, -500, 10))
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
            if event.key == pygame.K_c:
                particles = []
    if flag:
        if counter % speed == 0:
            particles = particleloop(particles, objects)
            #objects = mainloop(objects)
        counter += 1
    if flag2:
        flow(objects)

    for each in particles:
        each.drawparticle()

    for count, each in enumerate(objects):
        each.drawplanet()
        if (each.xpos,each.ypos,count) not in total:
            total.append((each.xpos, each.ypos, count))


    fpsClock.tick(60)
    pygame.display.update()
