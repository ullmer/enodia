# Enodia + ACCelerate visualization controllers class 
# Brygg Ullmer, Clemson University
# Begun in-class as pgzImg03.py on 2022-03-29; forked 2022-04-03

import yaml, sys, os, traceback
import pygame
from pgzero.builtins import Actor, animate, keyboard

from enoButton  import *
from enoActor   import *
from enoSpreads import *

####################################################################
############ Enodia/ACCelerate visualization controller ############

class enoAcclVizController:

  panel1Fn = 'yaml/accl01Panel.yaml'
  panel1F, panel1Y, panel1YL  = [None]*3
  scrWidth, scrHeight         = [None]*2
  paperBandActors, touchElActors, spreadSelectorPanel = [None]*3
  espreadsL     = None
  windowSurface = None
  currentSelectAbbrev = None

  firstDrawIter = True
  dy = 50
  verbose = False
  colorbarDim = [50, 1080]
  alphaCover = False
  bcTouchIdx = 1
  drawTouchEls = 0

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
      self.panel1F  = open(self.panel1Fn, 'r')
      self.panel1Y  = yaml.safe_load(self.panel1F)
    except: self.warn("loadYaml caught error"); traceback.print_exc()

    if self.verbose: print(self.self.panel1Y)

  ####################### parse YAML #######################

  def parseYaml(self):

    if self.panel1Y is None:
      self.warn("parseYaml: no YAML struct found"); return -1

    try:
      self.spreadsYL = self.panel1Y["spreads"]  #list of spreads

      #for spreadName in self.spreadsYL:
      #  newSpread = enoSpread(spreadName)
      #  self.spreadsL.append(newSpread)

      self.espreadsL = []
      newSpread      = enoSpread("accBC2", bcTouchIdx = self.bcTouchIdx, drawTouchEls=self.drawTouchEls)
      self.espreadsL.append(newSpread)

      self.spreadSelectorPanel = []

      #for row in self.spreadsYL:
      ba = enoButtonArray(self.spreadsYL, buttonDim=(250, 30), dx=0, dy=40, 
                          basePos=(1650, 425))
                          #basePos=(1650, 225))
      self.spreadSelectorPanel.append(ba)

    except: 
      self.warn("parseYaml: problems parsing YAML"); traceback.print_exc()

  ####################### initialize visuals #######################

  def initViz(self):
    #pb1    = Actor('d6/pband/simap16e-ub', topleft=(0,0))    #upper paper band
    #pb2    = Actor('d6/pband/simap16e-lb', topleft=(0,214+1080/6))

    #ea1    = enoActor("acc_bc/x1/abc32c-bau-to", basePos = (30, 327))
    #ea2    = enoActor("acc_bc/x1/abc32c-mkk-to", basePos = (85, 327))

    #self.paperBandActors = [pb1, pb2]
    self.paperBandActors = []
    self.touchElActors   = []
    #self.touchElActors   = [ea1, ea2]

  ################# draw transp black overlay #################

  def drawTranspOverlayLower(self, shimPos):
    #olDim = self.transpOverlayLowerDim
    #olPos = self.transpOverlayLowerPos

    #print("drawTranspOverlayLower:", shimPos)

    olDim = (1920, 140)
    olPos = (0,    255)
    #if not isinstance(shimPos, tuple):
    #  self.warn("drawTranspOverlayLower: shimpos is not tuple"); return

    olPosShimmed = (olPos[0] + shimPos[0], olPos[1] + shimPos[1])

    s = pygame.Surface(olDim) # (1000,750)  the size of your rect
    s.set_alpha(150)          # alpha level
    s.fill((0,0,0))           # this fills the entire surface
    #s.fill((200,200,200))           # this fills the entire surface
    self.windowSurface.blit(s, olPosShimmed)

    # https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangles-and-polygons-in-pygame

  ################# draw transp colorbar overlay #################

  def drawTranspColorbar(self, barColor, barPosition):
    cbDim = self.colorbarDim
    olPos = (0,    255)

    olPos = (barPosition, 0)

    s = pygame.Surface(cbDim) # (1000,750)  the size of your rect
    s.set_alpha(200)          # alpha level
    s.fill(barColor)
    self.windowSurface.blit(s, olPos)

  ################# draw #################

  def draw(self, screen): 

    if self.firstDrawIter:
      swh = (self.scrWidth, self.scrHeight)
      #scr = pygame.display.set_mode(swh, pygame.FULLSCREEN|pygame.HWSURFACE)
      self.windowSurface = pygame.display.set_mode(swh, pygame.NOFRAME|pygame.HWSURFACE)
      #scr = pygame.display.set_mode(swh, pygame.NOFRAME)
      self.firstDrawIter = False

    screen.clear()
    for pba in self.paperBandActors: pba.draw()
    if self.drawTouchEls:
      for tea in self.touchElActors:       tea.draw() 

    #if self.spreadSelectorPanel is not None:
    #  for ssp in self.spreadSelectorPanel: ssp.draw(screen)

    #for es  in self.espreadsL:           es.draw()

    if self.espreadsL is not None:
      for es  in self.espreadsL:           es.draw(self)
      #for es  in self.espreadsL:           es.draw(self.drawTranspOverlayLower)

    #if self.alphaCover: self.drawTranspOverlayLower()

  ################# mouse down #################

  def on_mouse_down(self, pos):
    self.alphaCover = True
    #for pba in self.paperBandActors: pba.on_mouse_down(pos)

    if self.drawTouchEls:
      for tea in self.touchElActors:       tea.on_mouse_down(pos)

    for ssp in self.spreadSelectorPanel: ssp.on_mouse_down(pos)
    for es  in self.espreadsL:           es.on_mouse_down(pos)

### end ###
