'''
Created on 2013-07-04

@author: chris_000
'''

import pyglet
from pyglet.window import key
import car

class Window(pyglet.window.Window):
    def __init__(self, sim):
        super(Window, self).__init__()
        self.set_caption("Car Physics")
        self.set_size(800,600)
        self.sim = sim
        
    def on_draw(self):
        self.clear()
        self.sim.draw()

class RaceSim(object):
    def __init__(self):
        self.window = Window(self)
        self.batch = pyglet.graphics.Batch()
        self.keys = key.KeyStateHandler()
        self.window.push_handlers(self.keys)
        self.initsim()
        pyglet.clock.schedule_interval(self.update, 1/60.)
        
    def initsim(self):
        self.car = car.Car(self)
        self.car.x = 200
        self.car.y = 200
        self.car.batch = self.batch
    
    def update(self, dt):
        self.car.update()
        
    def draw(self):
        self.batch.draw()

sim = RaceSim()
pyglet.app.run()
