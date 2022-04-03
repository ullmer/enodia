# Enodia + ACCelerate visualization controllers class 
# Brygg Ullmer, Clemson University
# Begun in-class as pgzImg03.py on 2022-03-29; forked 2022-04-03

import yaml, sys, os, platform
import pygame
from enoButton import *
from enoActor  import *

####################################################################
############ Enodia/ACCelerate visualization controller ############

class enoAcclVizController:

  panel1Fn = 'panel03.yaml'
  panel1F  = None
  panel1Y  = None

  panel = []

  dy = 50; idx = 0

  ####################### constructor #######################

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml()
    self.parseYaml()

  ####################### constructor #######################

  def warn(self, msg):
    try: print("enoAcclVizController warning:", msg)
    except: pass

  ####################### load YAML #######################

  def loadYaml(self):

    try:
      self.panel1F  = open(panel1Fn, 'r+t')
      self.panel1Y  = yaml.safe_load(self.panel1F)
    except: warn("loadYaml caught error")

    print(self.spreadsY)

  ####################### parse YAML #######################

  def parseYaml(self):

    if self.panel1Y is None:
      warn("parseYaml: no YAML struct found); return -1

    self.spreadsL = []
    try:
      self.spreadsYL = self.spreadsY["spreads"]  #list of spreads
      for spreadName in self.spreadsYL:
        newSpread = enoSpread(spreadName)
        self.spreadsL.append(newSpread)

    except: print("enoSpreads parseYaml: problems parsing YAML"); traceback.print_exc()



for row in panel1Y["spreads"]: #rows
  ba = enoButtonArray(row, buttonDim=(250, 30), dx=0, dy=40, 
                           basePos=(1650, 225))
  panel.append(ba); idx += 1

global actor1, targetpos, nextstate 
targetpos1 = (50, 50)
targetpos2 = (300, 300)
nextstate  = 0

################# next #################

def next():
  global nextstate, actor1
  if nextstate == 0:
    nextstate = 1; 
    animate(actor1, topleft=targetpos1, tween='accel_decel', on_finished=next)
  else:
    nextstate = 0; 
    animate(actor1, topleft=targetpos2, tween='accel_decel', on_finished=next)

################# draw #################

firstDrawIter = True

def draw(): 
  global panel, actors, eactors, firstDrawIter, WIDTH, HEIGHT

  if firstDrawIter:
    #scr = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    scr = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    firstDrawIter = False

  screen.clear()
  for actor  in actors:  actor.draw()
  for eactor in eactors: eactor.draw() #integrates enodia interactivity
  for ba in panel: ba.draw(screen)

################# mouse down #################

def on_mouse_down(pos):
  global panel, eactors
  for ba in panel:   ba.on_mouse_down(pos)
  for ea in eactors: ea.on_mouse_down(pos)

################# main #################

global actors, eactors
#actor1 = Actor('bb05', topleft=targetpos1)
pb1    = Actor('d6/pband/simap16e-ub', topleft=(0,0))    #upper paper band
pb2    = Actor('d6/pband/simap16e-lb', topleft=(0,214+1080/6))

ea1    = enoActor("acc_bc/d1/abc32c-bau", basePos = (30, 327))
ea2    = enoActor("acc_bc/d1/abc32c-mkk", basePos = (85, 327))

actors  = [pb1, pb2]
eactors = [ea1, ea2]
#animate(actor1, topleft=targetpos2, tween='accel_decel', on_finished=next)

#import pgzrun
#pgzrun.go()
### end ###
