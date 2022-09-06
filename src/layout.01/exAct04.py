# Enodia Fargate planner
# Brygg Ullmer, Clemson University
# Begun 2022-09-05

WIDTH  = 1920
HEIGHT = 1024

import math

fn2 = "person01f"
fn1 = "mri-fargate-08h-overlay1b"

apos         = (150, 150)
currentAngle = 0.

lastMouseLoc = None
rimTouched   = None

a1, a2 = Actor(fn1, pos=apos), Actor(fn2, pos=apos)
actors = [a2, a1]

################# draw #################

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()

################# on keyboard down #################

def on_key_down(): 
  dp = 150 #delta position

  if keyboard.lshift == True or keyboard.rshift == True:
    if keyboard.left:  rotActor(a2,  45)
    if keyboard.right: rotActor(a2, -45)
  else:
    if keyboard.left:  shiftActors([a1, a2], -dp,   0)
    if keyboard.right: shiftActors([a1, a2],  dp,   0)
    if keyboard.up:    shiftActors([a1, a2],   0, -dp)
    if keyboard.down:  shiftActors([a1, a2],   0,  dp)

################# rotate actor #################

def rotActor(whichActor, whichRot):
  global currentAngle

  currentAngle += whichRot
  animate(whichActor, angle=currentAngle, tween='accel_decel', duration=.3)

################# shift actor #################

def shiftActors(whichActors, dx, dy):
  global apos
  x, y = apos[0] + dx, apos[1] + dy; newPos = (x,y)
  apos = newPos

  for whichActor in whichActors:
    animate(whichActor, pos=newPos, tween='accel_decel', duration=.3)

################# mouse down #################

rotYAdj   = 12
selThresh = 47

def on_mouse_down(pos):
  global lastMouseLoc, rimTouched
  x, y = pos; pos2 = [x, y + rotYAdj]

  dist1 = math.dist(pos,  apos) 
  dist2 = math.dist(pos2, apos) 

  rimTouched = (dist1 > 110 and dist1 < 140)
  rotTouched = (dist2 < selThresh)
  #lbendTouched = 

  if rotTouched: 
    if x > apos[0]: rotActor(a2, -45)
    else:           rotActor(a2,  45)

  if rimTouched:
    lastMouseLoc = pos

################# mouse up #################

def on_mouse_move(pos):
  global lastMouseLoc, rimTouched
  if rimTouched:
    dx = pos[0] - lastMouseLoc[0]
    dy = pos[1] - lastMouseLoc[1]
    x, y = a1.pos[0] + dx, a1.pos[1] + dy; newPos = (x, y)
    a1.pos = newPos; a2.pos = newPos
    lastMouseLoc = pos

################# mouse up #################

def on_mouse_up():
  global origMousePressLoc, rimTouched
  origMousePressLoc = None
  rimTouched        = False

### end ###
