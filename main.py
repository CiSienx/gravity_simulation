import numpy as np 
import pygame as pg 
import keyboard as key
import random

size = (1000,700)
screen = pg.display.set_mode(size)
time = 5

def control():
    if key.is_pressed('q'):
        global time
        time *=  1.005
        print(time)
    if key.is_pressed('w'):
        time /= 1.005
        print(time)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

class planets :
    def __init__(self,screen,mass,color,pos):
        self.screen = screen
        self.mass = mass
        self.color = color
        self.Ux = random.uniform(-10000,0)
        self.Uy = random.uniform(-10000,0)
        self.pos = pos
        self.trail = []

    def move(self,F,time):
        a_x = F[0]/self.mass
        a_y = F[1]/self.mass

        self.Ux += a_x * time/2
        self.Uy += a_y * time/2

        dx = self.Ux * time + 0.5 * a_x * np.square(time)
        dy = self.Uy * time + 0.5 * a_y * np.square(time)

        self.Ux += a_x * time/2
        self.Uy += a_y * time/2

        self.pos = (self.pos[0] + dx/10000, self.pos[1] + dy/10000)


    def draw(self,volume):
        spos = (self.pos[0]/10,self.pos[1]/10)
        self.trail.append(spos)
        pg.draw.circle(self.screen,self.color,spos, volume)
        if len(self.trail) > 200:
            self.trail.pop(0)
        for i in range(len(self.trail)-2):
            pg.draw.line(self.screen,self.color,self.trail[i],self.trail[i + 1])

def Forces(planet_list):
    force_list = []
    G = -10
    for i in range(len(planet_list)):
        Fx = 0
        Fy = 0
        for j in range(len(planet_list)):
            if i != j:
                dx = planet_list[j].pos[0] - planet_list[i].pos[0]
                dy = planet_list[j].pos[1] - planet_list[i].pos[1]
                r2 = np.square(dx) + np.square(dy)
                if r2 != 0:
                    F = G * planet_list[i].mass * planet_list[j].mass / r2
                else:
                    F = 0
                    print("boom")
                Fx += F * dx / np.sqrt(r2)
                Fy += F * dy / np.sqrt(r2)
        force_list.append((Fx,Fy))
    return force_list

def perspective(planet,planet_list):
    px = 5000 - planet.pos[0]
    py = 3500 - planet.pos[1]
    for oplanet in planet_list:
        oplanet.pos = (px + oplanet.pos[0], py + oplanet.pos[1])

while True:
    x11 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x12 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x13 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x14 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x1 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x2 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x3 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x4 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x5 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x6 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x7 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x8 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x9 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x10 = planets(screen,1000000,(10,100,200),(random.randint(4000,8000),random.randint(2000,6000)))
    x15 = planets(screen,1000000,(10,100,200),(random.randint(0,1000),random.randint(0,700)))
    p1 = planets(screen,-15000000,(250,250,150),(5000,3500))
    planet_list = [p1,x11,x12,x13,x14,x15,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    while True:
        control()
        screen.fill((0,0,0))
        perspective(p1,planet_list)
        
        forces_list = Forces(planet_list)
        for planet in range(len(planet_list)):
            planet_list[planet].move(forces_list[planet],time)

        for planet in range(len(planet_list)):
            planet_list[planet].draw(7)
        p1.draw(20)

        if key.is_pressed("x"):
            break
        pg.display.flip()
