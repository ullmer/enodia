# Lilleken & Brygg
# Begun 2022-05-16

WIDTH  = 800
HEIGHT = 800

from enoDigits import *

T = "accel_decel" # accelerate, then decelerate animation
D = .2            # 1/5 of a second

rr = Actor('redrocket1')
rr.pos = 100, 700

ed = enoDigits(screen)
ed.introduceNumber(42, (100, 100))
ed.introduceNumber(11, (70, 70))

def draw(): #main drawing loop
  screen.clear()
  rr.draw()
  ed.drawNumbers()

def on_key_down(key, mod, unicode):
  x, y = rr.center
  
  if key == keys.LEFT:  animate(rr, center=(x-50, y),   tween=T, duration=D)
  if key == keys.RIGHT: animate(rr, center=(x+50, y),   tween=T, duration=D)
  if key == keys.SPACE: animate(rr, center=(x, y-1000), tween=T, duration=D)

### end ###
