# Enodia Fargate planner
# Brygg Ullmer, Clemson University
# Begun 2022-09-05

import math
import yaml
from pgzero.builtins import Actor, animate, keyboard

################################################################
################# Enodia Screen Ensemble Class #################

class enoScrEnsemble:

  glyphFn1 = "mri-fargate-08h-overlay1b"
  glyphFn2 = "person03f"
  #glyphFn2 = "mri-fargate-08b2b"
  
  currentPos      = (150, 150)
  currentAngle    = 0.
  deltaPos        = 150 #delta position
  deltaAngle      = 45  #delta angle
  rotYAdj         = 12
  rotSelectThresh = 47
  rimInnerThresh  = 110
  rimOuterThresh  = 140
  highlightMgr    = None
  
  lastMouseLoc   = None
  elTouched      = None

  actor1, actor2 = None, None
  actors         = None
  muteInput      = False
  
  ################# constructor #################
  
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.buildVisuals()

  ################# getPos #################
  
  def getPos(self): return self.currentPos

  ################# buildVisuals #################
  
  def buildVisuals(self): 
    self.actor1 = Actor(self.glyphFn1, pos=self.currentPos)
    self.actor2 = Actor(self.glyphFn2, pos=self.currentPos)
    self.actors = [self.actor2, self.actor1]
  
  ################# draw #################
  
  def draw(self): 
    for actor in self.actors: actor.draw()
  
  ################# on keyboard down #################
  
  def on_key_down(self): 
    if self.muteInput: return

    a1, a2 = self.actor1, self.actor2; dp = self.deltaPos
  
    if keyboard.lshift == True or keyboard.rshift == True:
      if keyboard.left:  self.rotActor(a2,  self.deltaAngle)
      if keyboard.right: self.rotActor(a2, -self.deltaAngle)
    else:
      if keyboard.left:  self.shiftActors([a1, a2], -dp,   0)
      if keyboard.right: self.shiftActors([a1, a2],  dp,   0)
      if keyboard.up:    self.shiftActors([a1, a2],   0, -dp)
      if keyboard.down:  self.shiftActors([a1, a2],   0,  dp)
  
  ################# rotate actor #################
  
  def rotActor(self, whichActor, whichRot):
    self.currentAngle += whichRot
    animate(whichActor, angle=self.currentAngle, tween='accel_decel', duration=.3)
  
  ################# shift actor #################
  
  def shiftActors(self, whichActors, dx, dy):
    x, y = self.currentPos[0] + dx, self.currentPos[1] + dy; newPos = (x,y)
    self.currentPos = newPos
  
    for whichActor in whichActors:
      animate(whichActor, pos=newPos, tween='accel_decel', duration=.3)
  
  ################# mouse down #################
  
  def on_mouse_down(self, pos):
    x, y = pos; pos2 = [x, y + self.rotYAdj]
  
    dist1 = math.dist(pos,  self.currentPos) 
    dist2 = math.dist(pos2, self.currentPos) 
  
    self.elTouched = dist1 < self.rimOuterThresh
  
    if self.elTouched:
      self.lastMouseLoc = pos
      if self.highlightMgr is not None: self.highlightMgr.highlightByHandle(self, 0.1)
  
  ################# mouse up #################
  
  def on_mouse_move(self, pos):
    if self.muteInput: return

    if self.elTouched:
      a1 = self.actor1
      dx = pos[0] - self.lastMouseLoc[0]
      dy = pos[1] - self.lastMouseLoc[1]
      x, y = a1.pos[0] + dx, a1.pos[1] + dy; newPos = (x, y)
      self.actor1.pos = newPos
      self.actor2.pos = newPos
      self.currentPos = newPos
      self.lastMouseLoc = pos
  
  ################# mouse up #################
  
  def on_mouse_up(self):
    if self.muteInput: return

    self.lastMouseLoc = None
    self.elTouched   = False

######################################################################
################# Enodia scrEnsemble Highlight Class #################

class enoSEhighlight:
  glyphFn1   = "mri-fargate-09a-highlight2"
  actor      = None
  currentPos = (150, 150)
  currentLetterVal = 97 #ASCII for 'a'
  currentHighlight = None
  lastMouseLoc     = None
  deltaPos         = 150 #delta position

  hlDictByKey    = None # Dictionary of highlightable entities, single-letter key to object handle
  hlDictByHandle = None # Dictionary of highlightable entities, object handle to single-letter key
  
  ################# constructor #################
  
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.buildVisuals()
    self.hlDictByKey    = {}
    self.hlDictByHandle = {}

  ################# buildVisuals #################
  
  def buildVisuals(self): 
    self.actor = Actor(self.glyphFn1, pos=self.currentPos)

  ################# register highlightable element #################
  
  def registerHl(self, element, muteInput = False):

    keybind = chr(self.currentLetterVal)

    self.hlDictByKey[keybind]    = element
    self.hlDictByHandle[element] = keybind

    if muteInput: element.muteInput = True
    element.highlightMgr = self

    self.currentLetterVal += 1
    return keybind

  ################# draw #################
  
  def draw(self): 
    self.actor.draw()
  
  ################# on keyboard down #################
  
  def on_key_down(self): 
    keys = self.hlDictByKey.keys()
    for key in keys:
      if keyboard.__getattr__(key): self.highlightByKey(key)

    a1 = self.actor; dp = self.deltaPos
  
    if keyboard.lshift == False and keyboard.rshift == False:
      if keyboard.left:  self.shiftActors([a1], -dp,   0)
      if keyboard.right: self.shiftActors([a1],  dp,   0)
      if keyboard.up:    self.shiftActors([a1],   0, -dp)
      if keyboard.down:  self.shiftActors([a1],   0,  dp)

  ################# shift actor #################
  
  def shiftActors(self, whichActors, dx, dy):
    x, y = self.currentPos[0] + dx, self.currentPos[1] + dy; newPos = (x,y)
    self.currentPos = newPos
  
    animate(self.actor, pos=newPos, tween='accel_decel', duration=.3)

  ################# highlightByHandle #################
  
  def highlightByHandle(self, handle, duration=.3):
    if handle not in self.hlDictByHandle:
      print("enoSEhighlight highlightByHandle: handle not found"); return
    key = self.hlDictByHandle[handle]
    self.highlightByKey(key, duration)

  ################# highlight #################
  
  def highlightByKey(self, whichKey, animDuration=.3):
    if self.currentHighlight is not None:
      chl = self.hlDictByKey[self.currentHighlight]
      chl.muteInput = True

    self.currentHighlight = whichKey
    whichElement          = self.hlDictByKey[whichKey]
    highlightNewPos       = whichElement.getPos()
    animate(self.actor, pos=highlightNewPos, tween='accel_decel', duration=animDuration)
    whichElement.muteInput = False

  def on_mouse_down(self, pos): self.lastMouseLoc = pos
  def on_mouse_up(self):        self.lastMouseLoc = None
  def on_mouse_move(self, pos): 
    if self.lastMouseLoc == None: return
    a1 = self.actor
    dx = pos[0] - self.lastMouseLoc[0]
    dy = pos[1] - self.lastMouseLoc[1]
    x, y = a1.pos[0] + dx, a1.pos[1] + dy; newPos = (x, y)
    self.actor.pos    = newPos
    self.currentPos   = newPos
    self.lastMouseLoc = pos


######################################################################
################# Enodia scrEnsemble Highlight Class #################

class enoSceneManager: 
  yamlD = None #yaml data

  ################# constructor #################
  
  def __init__(self, yamlFn, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.parseYamlFn(yamlFn)

  ################# parse yaml filename #################
  
  def parseYamlFn(self, yamlFn):
    yf = open(yamlFn, 'rt')
    self.yamlD = yaml.safe_load(yf)
    print(self.yamlD)

      

### end ###
