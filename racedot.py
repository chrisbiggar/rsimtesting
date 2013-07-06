'''
Created on 2013-07-04

@author: chris_000
'''

import pyglet
from pyglet.window import key
import car

class RaceSim(pyglet.window.Window):
    def __init__(self):
        super(RaceSim, self).__init__()
        self.set_caption("Car Physics")
        self.batch = pyglet.graphics.Batch()
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        
    def on_draw(self):
        self.clear()
        self.batch.draw()

sim = RaceSim()
'''init res'''
car = car.Car(sim)
car.batch = sim.batch
car.x = 200
car.y = 200

'''@win.event
def on_key_press(symbol, modifiers):
    pass'''
        
def update(self):
    car.update()
    
    '''if sim.keys[key.DOWN]:
        print "space"'''
        
'''@win.event
def on_draw():
    win.clear()
    batch.draw()'''
    
pyglet.clock.schedule_interval(update, 1/60.)
pyglet.app.run()