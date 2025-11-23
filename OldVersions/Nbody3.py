import sys
import random
import pygame
from pygame.locals import *
import math
from pygame import gfxdraw
from copy import deepcopy
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
width, height = 1700,900
screen = pygame.display.set_mode((width,height))
gcons = 7
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
        self.forcesx = []
        self.forcesy = []
    def drawplanet(self):
        if flag3:
            #print(self.xpos,self.ypos)
            pygame.draw.circle(screen, white, (round(self.xpos), round(self.ypos)), self.radius, 0)

    def moveplanet(self):
        self.fx = sum(self.forcesx)
        self.fy = sum(self.forcesy)

        self.accelx = self.fx / self.mass
        self.accely = self.fy / self.mass

        self.vx += self.accelx
        self.vy += self.accely

        self.xpos += self.vx
        self.ypos += self.vy

    def __eq__(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return True
        else:
            return False
objects = []
v = 4
objects = [Planet(850,450,0,0,500,10,True),Planet(850,250,v,0,500,10,True),Planet(850,650,-v,0,500,10,True),Planet(650,450,0,-v,500,10,True),Planet(1050,450,0,v,500,10,True)]
speed = 5
#objects = [Planet(900,450,0,0,35000,10,True), Planet(600,450,-7,-15,100,10,True),Planet(1200,450,7,15,100,10,True),Planet(900,150,15,-7,100,True),Planet(900,750,-15,7,100,10,True)]

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

steps = 5
def hitdetect(objs,steps):
    l = deepcopy(objs)
    for x in range(steps):

        rn1x,rn1y = set[0].xpos + set[0].vx * x/steps,set[0].ypos + set[0].vy * x/steps
        rn2x,rn2y = set[1].xpos + set[1].vx * x/steps,set[1].ypos + set[1].vy * x/steps
        dist = math.sqrt((rn1x - rn2x) ** 2 + (rn1y - rn2y) ** 2)
        if dist < set[0].radius + set[1].radius:
                print('hittt')
                            # flag = True
                        # l.remove(set[0])
                        # l.remove(set[1])
                        # l.append(Planet(    (set[0].xpos+set[1].xpos)/2,     (set[0].xpos+set[1].xpos)/2,    (set[0].vx * set[0].mass + set[1].vx * set[1].mass) / (set[0].mass +  set[1].mass),(set[0].vy * set[0].mass + set[1].vy * set[1].mass) / (set[0].mass +  set[1].mass),     set[0].mass +  set[1].mass,     math.sqrt(set[0].radius**2 + set[1].radius**2),True ))
                        # break
        return l

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
import itertools
# x,y , v1x , v1y, mass , radius, hit?
point = 5
def mainloop(lis):
    objs = lis
    for each in lis:
        each.forcesy,each.forcesx = [],[]

        if each.xpos < -20 or each.xpos > 1820 or each.ypos < -20 or each.ypos > 920:
            objs.remove(each)

    for set in itertools.combinations(objs, 2):
        dirx = int(set[0].xpos - set[1].xpos)
        diry = int(set[0].ypos - set[1].ypos)
        gforce = gcons * (set[0].mass * set[1].mass) / ((math.sqrt(abs(dirx) ** 2 + abs(diry) ** 2)) ** 2)
        angle = math.degrees(math.atan2(diry, dirx))
        fy = math.sin(math.radians(angle)) * gforce
        fx = math.cos(math.radians(angle)) * gforce

        objs[objs.index(set[0])].forcesx.append(-fx)
        objs[objs.index(set[0])].forcesy.append(-fy)
        objs[objs.index(set[1])].forcesx.append(fx)
        objs[objs.index(set[1])].forcesy.append(fy)
    return objs



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
                objects.append(Planet(x,y,0,-10,100,10,True))
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

        objects = mainloop(objects)
        #objects = hitdetect(objects,steps)
        for each in objects:
            each.moveplanet()

        counter += 1
    if flag2:
        flow(objects)
    # if len(total) > 2000:
    #     total.remove(total[0])
    for count,each in enumerate(objects):
        each.drawplanet()
        total.append((each.xpos,each.ypos))
    #objects = hitdetect(objects)
    for counter,each in enumerate(total):
        screen.set_at((int(each[0]), int(each[1])), (255, 255, 255))


    fpsClock.tick(60)
    pygame.display.update()