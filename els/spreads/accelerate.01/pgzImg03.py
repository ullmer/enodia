# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import yaml, sys, os, platform
import pygame
from enoButton import *
from enoActor  import *

WIDTH  = 1920
HEIGHT = int(214*2+1080/6)
winPos = (-2050, 0) #note this is for a multi-screen setup, and might make
                    #invisible on a single-screen box

#https://stackoverflow.com/questions/57674156/how-to-move-a-no-frame-pygame-windows-when-user-click-on-it/57681853#57681853

if platform.system() is "Windows": 
  from ctypes import windll 
  hwnd = pygame.display.get_wm_info()['window']
  windll.user32.MoveWindow(hwnd, winPos[0], winPos[1], WIDTH, HEIGHT, False)

#w, h = pygame.display.get_surface().get_size()
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % winPos
#os.environ['SDL_VIDEO_CENTERED'] = '1'

panel1Fn = 'panel03.yaml'
panel1F  = open(panel1Fn, 'r+t')
panel1Y  = yaml.safe_load(panel1F)
#panel1Y  = yaml.load(panel1F)

#print(panel1Y)
#sys.exit(-1)

global panel
panel = []

dy = 50; idx = 0

for row in panel1Y["spreads"]: #rows
  ba = enoButtonArray(row, buttonDim=(250, 30), dx=0, dy=40, 
                           basePos=(1650, 225))
  panel.append(ba); idx += 1

global actor1, targetpos, nextstate 
targetpos1 = (50, 50)
targetpos2 = (300, 300)
nextstate  = 0

################# next #################

def next():
  global nextstate, actor1
  if nextstate == 0:
    nextstate = 1; 
    animate(actor1, topleft=targetpos1, tween='accel_decel', on_finished=next)
  else:
    nextstate = 0; 
    animate(actor1, topleft=targetpos2, tween='accel_decel', on_finished=next)

################# draw #################

firstDrawIter = True

def draw(): 
  global panel, actors, eactors, firstDrawIter, WIDTH, HEIGHT

  if firstDrawIter:
    #scr = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    scr = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    firstDrawIter = False

  screen.clear()
  for actor  in actors:  actor.draw()
  for eactor in eactors: eactor.draw() #integrates enodia interactivity
  for ba in panel: ba.draw(screen)

################# mouse down #################

def on_mouse_down(pos):
  global panel, eactors
  for ba in panel:   ba.on_mouse_down(pos)
  for ea in eactors: ea.on_mouse_down(pos)

################# main #################

global actors, eactors
#actor1 = Actor('bb05', topleft=targetpos1)
pb1    = Actor('d6/pband/simap16e-ub', topleft=(0,0))    #upper paper band
pb2    = Actor('d6/pband/simap16e-lb', topleft=(0,214+1080/6))

ea1    = enoActor("acc_bc/d1/abc32c-bau", basePos = (30, 327))
ea2    = enoActor("acc_bc/d1/abc32c-mkk", basePos = (85, 327))

actors  = [pb1, pb2]
eactors = [ea1, ea2]
#animate(actor1, topleft=targetpos2, tween='accel_decel', on_finished=next)

#import pgzrun
#pgzrun.go()
### end ###
