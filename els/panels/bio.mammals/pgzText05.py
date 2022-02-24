# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from enoButton import *
import yaml

WIDTH=600
HEIGHT=600

global ba1 

panel1Fn = 'panel1.yaml'
panel1F  = open(panel1Fn, 'r+t')
panel1Y  = yaml.safe_load(panel1F)

#baText = ['CECAS', 'AAH', 'SCIENCE']
ba1 = enoButtonArray(baText, buttonDim=(150, 30), dx=160)

def draw(): 
  global ba1 
  ba1.draw(screen)

def on_mouse_down(pos):
  global ba1
  ba1.on_mouse_down(pos)

### end ###
