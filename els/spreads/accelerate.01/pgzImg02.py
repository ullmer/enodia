# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from enoButton import *
import yaml

WIDTH=900
HEIGHT=600

panel1Fn = 'panel1.yaml'
panel1F  = open(panel1Fn, 'r+t')
panel1Y  = yaml.safe_load(panel1F)

print(panel1Y)

global panel
panel = []

dy = 50; idx = 0

for row in panel1Y: #rows
  ba = enoButtonArray(row, buttonDim=(150, 30), dx=160, 
                           basePos=(0, dy*idx))
  panel.append(ba); idx += 1

global actor1, targetpos, nextstate 
targetpos1 = (50, 50)
targetpos2 = (300, 300)
nextstate  = 0

################# next #################

def next():
  global nextstate, actor1
  if nextstate == 0:
    nextstate = 1; animate(actor1, topleft=targetpos1, tween='accel_decel', on_finished=next)
  else:
    nextstate = 0; animate(actor1, topleft=targetpos2, tween='accel_decel', on_finished=next)

################# draw #################

def draw(): 
  global panel, actors

  screen.clear()
  for actor in actors: actor.draw()
  for ba in panel: ba.draw(screen)

################# mouse down #################

def on_mouse_down(pos):
  global panel
  for ba in panel: ba.on_mouse_down(pos)

################# main #################

global actors
actor1 = Actor('bb05', topleft=targetpos1)
pb1    = Actor('d6/pband/siMap16e-ub', topleft=(0,0))    #upper paper band
pb2    = Actor('d6/pband/siMap16e-lb', topleft=(0,360))

actors = [actor1, pb1, pb2]
animate(actor1, topleft=targetpos2, tween='accel_decel', on_finished=next)

### end ###
