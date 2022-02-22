# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from pgzButton import *

WIDTH=600
HEIGHT=600

global ba1 
baText = ['a', 'b', 'c']
ba1 = pgzButtonArray(baText)

def draw(): 
  global ba1 
  ba1.draw(screen)

### end ###
