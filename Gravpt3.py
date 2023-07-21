import sys
import random

import numba
import numpy
import pygame
from pygame.locals import *
import math
from pygame import gfxdraw
from copy import deepcopy
from numba import jit
import numpy as np
import numba
from PIL import Image

import time
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
gcons = 5
n = 10
o = 0
class Planet():
    def __init__(self,xpos,ypos,vx,vy,mass):

        self.xpos = int(xpos)
        self.ypos = int(ypos)
        self.vx = int(vx)
        self.vy = int(vy)
        self.mass = mass
        self.forces = []




    def __eq__(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return True
        else:
            return False
class Particle():
    def __init__(self, xi,yi,xpos, ypos, vx, vy, radius):
        self.xi = xi
        self.yi = yi
        self.xpos = int(xpos)
        self.ypos = int(ypos)
        self.vx = int(vx)
        self.mass = 1
        self.vy = int(vy)
        self.radius = radius


speed = 5
#objects = [Planet(700,450,0,0,5000),Planet(1100,450,0,0,5000)]
#objects = [Planet(800,450,0,0,-1000),Planet(1000,450,0,0,-1000),Planet(900,350,0,0,1000),Planet(900,550,0,0,1000)]
objects = [[800,450,0,0,100]]
fpsClock = pygame.time.Clock()
def backg1():
    screen.fill(black)

particles = []
for x in range(1800):
    for y in range(900):
        particles.append(Particle(x,y,x,y,0,0,1))

        #print(gforce,angle)
total = []

#xi,yi,x,y,vx,vy,rad PARTICLE
#x,y,vx,vy,m PLANET
# x,y , v1x , v1y, mass , radius, hit?
def mapcord(i, istart, iend, ostart, oend):
    return ostart + ((oend - ostart) / (iend - istart)) * (i - istart)

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
    final = deepcopy(newobjs)
    return final

# x,y , v1x , v1y, mass , radius, hit?

from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

for x in range(1):
    print(x)
    particles = particleloop(particles,objects)
fact = 1

counter = 0
pygame.init()
width, height = 1800,900
screen = pygame.display.set_mode((width,height))
#300 150
pygame.display.set_caption('Gravity')
counter = 0
world = []
for y in range(900):
    world.append([])
newt= time.time()
import time
while True:
    xcord, ycord = pygame.mouse.get_pos()
    backg1()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # print('NEXT ITER')
                # world = []
                # for x in range(1800):
                #     world.append([])
                #
                #     for y in range(900):
                #         world[x].append([])
                # print("WORLD DONE: ",len(world),len(world[x]))
                # for x in range(1800):
                #     for y in range(900):
                #         print(y,x)
                #         world[y][x].append(screen.get_at((x, y)))

                # print(len(world))
                # for x in world:
                #     print(len(x))
                #print("Image Saved")
                world = []
                for y in range(900):
                    world.append([])

                for each in particles:
                    dx = each.xi - each.xpos
                    dy = each.yi - each.ypos
                    dist = abs(math.sqrt(((dx ** 2) + (dy ** 2))))
                    # col = round(mapcord(dist,0,high,0,255)) + 1
                    col = round(abs(((math.log(dist + 1)) / (math.log(high / fact))) * 255))
                    if col > 255:
                        col = 255

                    world[each.yi].append([int(col),int(col),int(col)])
                newworld = np.asarray(world)
                #print(newworld)
                # IMIR = newworld.reshape(1800, 900)
                imgarray = array_to_img(newworld)

                imgarray.save(f"pic{time.time() }.jpeg")

                counter += 1
                particles = particleloop(particles, objects)
                print("Next level")
                newt = time.time()
    if time.time() - newt > 20:
        world = []
        for y in range(900):
            world.append([])

        for each in particles:
            dx = each.xi - each.xpos
            dy = each.yi - each.ypos
            dist = abs(math.sqrt(((dx ** 2) + (dy ** 2))))
            # col = round(mapcord(dist,0,high,0,255)) + 1
            col = round(abs(((math.log(dist + 1)) / (math.log(high / fact))) * 255))
            if col > 255:
                col = 255

            world[each.yi].append([int(col), int(col), int(col)])
        newworld = np.asarray(world)
        # print(newworld)
        # IMIR = newworld.reshape(1800, 900)
        imgarray = array_to_img(newworld)

        imgarray.save(f"pic{time.time()}.jpeg")

        counter += 1
        particles = particleloop(particles, objects)
        print("Next level")
        newt = time.time()
    else:
        print(time.time() - newt)



    high = 0
    for each in particles:
        dx = each.xi - each.xpos
        dy = each.yi - each.ypos
        dist = math.sqrt(((dx**2) + (dy**2)))
        if dist > high:
            high = int(dist)
    for each in particles:
        dx = each.xi - each.xpos
        dy = each.yi - each.ypos
        dist = abs(math.sqrt(((dx**2) + (dy**2))))
        #col = round(mapcord(dist,0,high,0,255)) + 1
        col = round(abs(((math.log(dist+1))/(math.log(high/fact))) * 255))
        if col > 255:
            col = 255
        #print(col)
        #print(high,dist,col)

        screen.set_at((each.xi, each.yi), (col, col, col))


    print(high)
    fpsClock.tick(60)
    pygame.display.update()