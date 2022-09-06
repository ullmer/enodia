# Enodia Fargate planner
# Brygg Ullmer, Clemson University
# Begun 2022-09-05

WIDTH  = 1920
HEIGHT = 1024

import math

fn1 = "mri-fargate-08b1b"
fn2 = "mri-fargate-08b2b"

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

  if keyboard.left:  rotActor(a2,  45)
  if keyboard.right: rotActor(a2, -45)

################# rotate actor #################

def rotActor(whichActor, whichRot):
  global currentAngle

  currentAngle += whichRot
  animate(whichActor, angle=currentAngle, tween='accel_decel', duration=.3)

################# mouse down #################

def on_mouse_down(pos):
  global lastMouseLoc, rimTouched
  dist1      = math.dist(pos,  apos) 
  rimTouched = (dist1 > 110 and dist1 < 140)

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
  global lastMouseLoc, rimTouched
  lastMouseLoc = None
  rimTouched   = False

### end ###
