# Enodia Fargate planner
# Brygg Ullmer, Clemson University
# Begun 2022-09-05

import math
from pgzero.builtins import Actor, animate, keyboard

################################################################
################# Enodia Screen Ensemble Class #################

class enoScrEnsemble:

  glyphFn1 = "mri-fargate-08h-overlay1b"
  glyphFn2 = "person01f"
  
  currentPos      = (150, 150)
  currentAngle    = 0.
  deltaPos        = 150 #delta position
  deltaAngle      = 45  #delta angle
  rotYAdj         = 12
  rotSelectThresh = 47
  rimInnerThresh  = 110
  rimOuterThresh  = 140
  
  lastMouseLoc   = None
  rimTouched     = None
  rotTouched     = None

  actor1, actor2 = None, None
  actors         = None
  
  ################# constructor #################
  
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.buildVisuals()

  ################# constructor #################
  
  def buildVisuals(self): 
    self.actor1 = Actor(self.glyphFn1, pos=self.currentPos)
    self.actor2 = Actor(self.glyphFn2, pos=self.currentPos)
    self.actors = [self.actor2, self.actor1]
  
  ################# draw #################
  
  def draw(self): 
    for actor in self.actors: actor.draw()
  
  ################# on keyboard down #################
  
  def on_key_down(self): 
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
  
    self.rimTouched = (dist1 > self.rimInnerThresh and dist1 < self.rimOuterThresh)
    self.rotTouched = (dist2 < self.rotSelectThresh)
    #lbendTouched = 
  
    if self.rotTouched: 
      if x > apos[0]: rotActor(a2, -self.deltaAngle)
      else:           rotActor(a2,  self.deltaAngle)
  
    if self.rimTouched:
      self.lastMouseLoc = pos
  
  ################# mouse up #################
  
  def on_mouse_move(self, pos):
    if self.rimTouched:
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
    self.lastMouseLoc = None
    self.rimTouched   = False
  
### end ###
