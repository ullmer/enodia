#PyGame Zero warmup on timelines
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

from pgzTimeline import *

pgzt = pgzTimeline("elements.yaml")

TITLE = "Timeline ex02f"
WIDTH = 1920; HEIGHT = 1080

def on_mouse_down(pos):
  global pgzt; pgzt.on_mouse_down(pos)

def draw():
  global pgzt
  screen.clear()
  pgzt.draw()

### end ###
