# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from pgzButton import *

WIDTH=600
HEIGHT=600

global but1
but1 = pgzButton("hello, world")

def draw(): 
  global but1
  but1.draw(screen)

### end ###
