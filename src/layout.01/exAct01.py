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

a1, a2 = Actor(fn1, pos=apos), Actor(fn2, pos=apos)
actors = [a2, a1]

################# draw #################

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()

################# on keyboard down #################

def on_key_down(): 
  if keyboard.left:  rotActor(a2,  45)
  if keyboard.right: rotActor(a2, -45)

################# rotate actor #################

def rotActor(whichActor, whichRot):
  global currentAngle

  currentAngle += whichRot
  animate(whichActor, angle=currentAngle, tween='accel_decel', duration=.3)

### end ###
