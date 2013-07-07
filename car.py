'''
Created on 2013-07-04

@author: chris_000
'''
import math
import pyglet
from pyglet.window import key
from pyglet.sprite import Sprite

class Car(Sprite):
    
    def __init__(self, sim):
        self.sim = sim
        '''position'''
        self.posz = 0.0
        '''velocity'''
        self.velx = 0.0
        self.vely = 0.0
        self.velz = 0.0
        
        self.speed = 0
        self.angle = 0
        
        self.dx = 25
        
        self.FRICTION = 2.
        self.POWER = 0.5
        self.MAXSPEED = 10
        
        '''sprite'''
        img = pyglet.image.load('res/car.png')
        Sprite.__init__(self, img)
        #self.batch = sim.batch
        self.rotation = 90
        
    def update(self):
        #print "update"
        if self.sim.keys[key.UP]:
            print "up"
            self.speed = 10
        elif self.sim.keys[key.DOWN]:
            print "down"
            self.speed = -10
        else:
            self.speed = 0
        if self.sim.keys[key.LEFT]:
            self.angle += 22.5
            self.rotation -= 22.5
        if self.sim.keys[key.RIGHT]:
            self.angle -= 22.5
            self.rotation += 22.5
            
        #if self.vely > 0:
            #self.vely -= self.friction
        
        '''if self.vely < 0:
            self.vely += self.friction
        elif self.vely > 0:
            self.vely -= self.friction'''
            
        #self.rotation = self.angle + 90
        
        scale_x = math.cos(math.radians(self.angle))
        scale_y = math.sin(math.radians(self.angle))
        self.velx = self.speed * scale_x
        self.vely = self.speed * scale_y
        
        self.x += self.velx
        self.y += self.vely
        self.posz += self.velz
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        