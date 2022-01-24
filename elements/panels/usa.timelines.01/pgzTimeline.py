#PyGame Zero timeline module
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

import yaml

###############################################################
######################### pgzTimeline #########################

class pgzTimeline:

  yfn    = 'elements.yaml'
  yf     = None
  yd     = None
  actors = None

  ######################### constructor #########################

  def __init__(self):
    self.actors = {}
    self.loadYaml()

  ######################### loadYaml #########################

  def loadYaml(self):
    try:
      self.yf  = open(self.yfn, 'r')
      self.yd  = yaml.safe_load(self.yf)

    except:

    try:
      for key in yd.keys():
        imgFn = yd[key]['img']
        x     = yd[key]['x']

        actors[key] = Actor(imgFn, topleft=(x, 10), opacity = .5)
    except:

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    for key in self.actors.keys():
      el = actors[key]
      if el.collidepoint(pos): 
        x, y = el.center
        animate(el, tween='accel_decel', pos=(x, y+100), duration=0.3)
  
######################### draw #########################

  def draw(self):
    for key in self.actors.keys():
      self.actors[key].draw()

### end ###
