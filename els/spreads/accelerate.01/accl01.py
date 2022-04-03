# Enodia + ACCelerate interactive visuals
# Brygg Ullmer, Clemson University
# Begun in-class as pgzImg03.py on 2022-03-29; forked 2022-04-03

import yaml, sys, os, platform
import pygame

from enoButton import *
from enoActor  import *
from enoAcclVizController import *

WIDTH  = 1920
HEIGHT = int(214*2+1080/6)
winPos = (-2050, 0) #note this is for a multi-screen setup, and might make
                    #invisible on a single-screen box

#https://stackoverflow.com/questions/57674156/how-to-move-a-no-frame-pygame-windows-when-user-click-on-it/57681853#57681853

if platform.system() == "Windows": 
  from ctypes import windll 
  hwnd = pygame.display.get_wm_info()['window']
  windll.user32.MoveWindow(hwnd, winPos[0], winPos[1], WIDTH, HEIGHT, False)

#w, h = pygame.display.get_surface().get_size()
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % winPos
#os.environ['SDL_VIDEO_CENTERED'] = '1'

eavc = enoAcclVizController(scrWidth=WIDTH, scrHeight=HEIGHT)

# Route draw, on_mouse_down pgzero event hooks to eavc

#eaa = enoActorArray(
#  basePos=(30, 327)

def draw():
  global eavc; global screen
  eavc.draw(screen)

def on_mouse_down(pos):
  global eavc
  eavc.on_mouse_down(pos)

### end ###
