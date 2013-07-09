'''
Created on 2013-07-04

@author: chris_000
'''
import pyglet
from carsim import simulation

class CarSimWindow(pyglet.window.Window):
    def __init__(self):
        super(CarSimWindow, self).__init__()
        self.set_caption("Car Physics")
        self.set_size(1800,920)
        self.set_location(60,60)
        self.sim = simulation.Simulation(self)
        
    def on_draw(self):
        self.clear()
        self.sim.draw()


sim = CarSimWindow()
pyglet.app.run()
