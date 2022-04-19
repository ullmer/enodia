# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

from ledArray    import *
from ledArrayViz import *

print("main called")

na = np2DCharArr((8,8))
na.fillRow(1, 'P')
na.fillCol(1, 'O')
na.fillRow(3, 'P')
#na.print()

global lav
lav = ledArrayViz(na)
  
def draw(): 
   global screen, lav
   try: lav.draw(screen)
   except: pass

### end ###
