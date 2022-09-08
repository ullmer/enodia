# Enodia Fargate planner
# Brygg Ullmer, Clemson University
# Begun 2022-09-05

WIDTH  = 1920
HEIGHT = 1024

import math
from enoScrEnsemble import *

a = 150
b = 500

coords = [(a, a), (a, b), (b, b), (b, a)]
actors = []

eseh = enoSEhighlight()
actors.append(eseh)

for coord in coords:
  ese    = enoScrEnsemble(currentPos=coord)
  actors.append(ese)
  eseh.registerHl(ese, True) #true = surpressInput

eseh.highlightByKey('a') #highlight the first

################# draw #################

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()

def on_key_down():      
  for actor in actors: actor.on_key_down()

def on_mouse_down(pos): 
  for actor in actors: actor.on_mouse_down(pos)

def on_mouse_move(pos): 
  for actor in actors: actor.on_mouse_move(pos)

def on_mouse_up():      
  for actor in actors: actor.on_mouse_up()

### end ###
