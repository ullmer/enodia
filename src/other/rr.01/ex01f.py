# Lilleken & Brygg
# Begun 2022-05-16

from enoNumbers import *
import random

from pgzero.game import screen
from pgzero.builtins import Actor, animate

WIDTH  = 800
HEIGHT = 800

T = "accel_decel" # accelerate, then decelerate animation
D = .2            # 1/5 of a second

rr = Actor('redrocket1')
rr.pos = 100, 700

ean = enoAnimNumbers(screen)
ean.introduceNumber(42, (120, 100))
ean.introduceNumber(11, (70, 70))
ean.animNumber(0, (400, 400))

def draw(): #main drawing loop
  screen.clear()
  rr.draw()
  ean.drawBubbledNumbers()

def on_key_down(key, mod, unicode):
  x, y = rr.center
  
  if key == keys.LEFT:  animate(rr, center=(x-50, y),   tween=T, duration=D)
  if key == keys.RIGHT: animate(rr, center=(x+50, y),   tween=T, duration=D)
  if key == keys.SPACE: animate(rr, center=(x, y-1000), tween=T, duration=D)

  if key == keys.PERIOD: 
    randomNum = random.randint(0, 13)
    rx, ry    = rr.pos

    n = ean.introduceNumber(randomNum, (rx, 800))
    ean.animNumber(n, (rx, 50))

### end ###
