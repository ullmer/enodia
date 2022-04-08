# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-01

import yaml, sys, traceback
from enoActor import *

###################################################################
####################### Enodia Spread Panel ####################### 

class enoPanelRotor(enoPanel):


 ####################### constructor #######################

  def __init__(self, spreadName, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__(spreadName, kwards)

### end ###
