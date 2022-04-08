# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-08

import yaml, sys, traceback
from enoActor import *
from pgzero.builtins import Actor, animate, keyboard

###################################################################
####################### Enodia Spread Panel ####################### 

class enoKbRotorHooks:

 ####################### constructor #######################

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

### end ###
