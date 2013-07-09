'''
Created on 2013-07-04

@author: chris_000
'''
import os
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
        
        self.FRICTION = 0.2
        self.POWER = 1
        self.BRAKEPOWER = 1.5
        self.MAXSPEED = 30
        
        '''sprite'''
        img = pyglet.image.load(os.path.join('res', 'car.png'))
        img.anchor_x = img.width / 2
        img.anchor_y = img.height / 4
        Sprite.__init__(self, img)
        #self.batch = sim.batch
        #self.rotation = 90
        
    def update(self):
        if self.sim.keys[key.UP]:
            if self.speed < self.MAXSPEED:
                self.speed += self.POWER
        elif self.sim.keys[key.DOWN]:
            if self.speed > 0:
                self.speed -= self.BRAKEPOWER
            else:
                self.speed = 0
        if self.sim.keys[key.LEFT]:
            if self.speed > 1:
                self.angle += 3.5
        if self.sim.keys[key.RIGHT]:
            if self.speed > 1:
                self.angle -= 3.5
            
        if self.speed > 0:
            self.speed -= self.FRICTION
            
        self.rotation = (360 - self.angle) + 90
        
        scale_x = math.cos(math.radians(self.angle))
        scale_y = math.sin(math.radians(self.angle))
        self.velx = self.speed * scale_x
        self.vely = self.speed * scale_y
        
        self.x += self.velx
        self.y += self.vely
        self.posz += self.velz
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        