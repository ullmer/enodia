#PyGame Zero warmup on timelines
#Brygg Ullmer, Clemson University
#Begun 2022-01-23

import yaml

yfn = 'elements.yaml'
yf  = open(yfn, 'r')
yd  = yaml.safe_load(yf)

actors = {}

for key in yd.keys():
  imgFn = yd[key]['img']
  x     = yd[key]['x']

  actors[key] = Actor(imgFn, topleft=(x, 10), opacity = .5)

TITLE = "Timeline ex02e"
WIDTH = 1920; HEIGHT = 1080

def on_mouse_down(pos):
  global actors
  for key in actors.keys():
    el = actors[key]
    if el.collidepoint(pos): 
      x, y = el.center
      animate(el, tween='accel_decel', pos=(x, y+100), duration=0.3)

def draw():
  global actors
  screen.clear()
  for key in actors.keys():
    actors[key].draw()

### end ###
