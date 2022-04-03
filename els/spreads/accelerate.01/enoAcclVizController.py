# Enodia + ACCelerate visualization controllers class 
# Brygg Ullmer, Clemson University
# Begun in-class as pgzImg03.py on 2022-03-29; forked 2022-04-03

import yaml, sys, os, traceback
import pygame
from enoButton import *
from enoActor  import *

####################################################################
############ Enodia/ACCelerate visualization controller ############

class enoAcclVizController:

  panel1Fn = 'panel03.yaml'
  panel1F, panel1Y, panel1YL  = [None]*3
  scrWidth, scrHeight         = [None]*2
  paperBandActors, touchElActors, spreadSelectorPanel = [None]*3

  firstDrawIter = True
  dy = 50

  ####################### constructor #######################

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml()
    self.parseYaml()
    self.initViz()

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

    try:
      self.spreadsYL = self.panel1Y["spreads"]  #list of spreads
      for spreadName in self.spreadsYL:
        newSpread = enoSpread(spreadName)
        self.spreadsL.append(newSpread)

      self.spreadSelectorPanel = []

      for row in self.spreadsYL:
        ba = enoButtonArray(row, buttonDim=(250, 30), dx=0, dy=40, 
                            basePos=(1650, 225))
        self.spreadSelectorPanel.append(self.ba)

    except: warn("parseYaml: problems parsing YAML"); traceback.print_exc()

  ####################### initialize visuals #######################

  def initViz(self):
    pb1    = Actor('d6/pband/simap16e-ub', topleft=(0,0))    #upper paper band
    pb2    = Actor('d6/pband/simap16e-lb', topleft=(0,214+1080/6))

    ea1    = enoActor("acc_bc/d1/abc32c-bau", basePos = (30, 327))
    ea2    = enoActor("acc_bc/d1/abc32c-mkk", basePos = (85, 327))

    self.paperBandActors = [pb1, pb2]
    self.touchElActors   = [ea1, ea2]

  ################# draw #################

  def draw(): 

    if self.firstDrawIter:
      #scr = pygame.display.set_mode((scrWidth, scrHeight), pygame.FULLSCREEN)
      scr = pygame.display.set_mode((scrWidth, scrHeight), pygame.NOFRAME)
      self.firstDrawIter = False

    screen.clear()
    for pba in self.paperBandActors: pba.draw()
    for tea in self.touchElActors:   tea.draw() #integrates enodia interactivity
    for ssp in self.spreadSelectorPanel: ssp.draw(screen)

  ################# mouse down #################

  def on_mouse_down(pos):

    for pba in self.paperBandActors: pba.on_mouse_down(pos)
    for tea in self.touchElActors:   tea.on_mouse_down(pos)
    for ssp in self.spreadSelectorPanel: ssp.on_mouse_down(pos)

### end ###
