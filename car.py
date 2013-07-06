'''
Created on 2013-07-04

@author: chris_000
'''
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
        
        self.dx = 25
        self.friction = 2.
        '''sprite'''
        img = pyglet.image.load('res/car.png')
        Sprite.__init__(self, img)
        
    def update(self):
        #print "update"
        if self.sim.keys[key.UP]:
            print "up"
            self.vely = 25
        if self.sim.keys[key.DOWN]:
            print "down"
            self.vely = -25
            
        if self.vely > 0:
            self.vely -= self.friction
        
        '''if self.vely < 0:
            self.vely += self.friction
        elif self.vely > 0:
            self.vely -= self.friction'''
        
        self.x += self.velx
        self.y += self.vely
        self.posz += self.velz
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        