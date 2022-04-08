# Enodia + ACCelerate visualization controllers class 
# Brygg Ullmer, Clemson University
# Begun in-class as pgzImg03.py on 2022-03-29; forked 2022-04-03

import yaml, sys, os, traceback
import pygame
from pgzero.builtins import Actor, animate, keyboard

from enoButton  import *
from enoActor   import *
from enoSpreads import *

####################################################################
############ Enodia/ACCelerate visualization controller ############

class enoAcclVizControllerRotor(enoAcclVizController):


  ####################### constructor #######################
  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    super().__init__(spreadName, kwards)

### end ###
