

import pyglet
from pyglet.window import key
import car


class Simulation(object):
    def __init__(self, window):
        self.window = window
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