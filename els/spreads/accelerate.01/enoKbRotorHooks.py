# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-08

import yaml, sys, traceback
from pgzero.builtins import Actor, animate, keyboard
from enoActor import *

###################################################################
####################### Enodia Spread Panel ####################### 

class enoKbRotorHooks:

 ####################### constructor #######################

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

 ####################### constructor #######################

 # def on_key_down(self, key, vizController):
 #   print("key:", key)
 #   #inputHooks.on_key_down(key, vizController)

 #   try:
 #     if key == keys.DALT: print("down")
 #     if key == keys.UALT: print("up")
 #     if key == keys.OALT: print("push")
 #   except: 
 #      print("on_key_down exception:")
 #      traceback.print_exc()


  def rotorDown(self, vizController): print("rotor down")
  def rotorUp(self, vizController):   print("rotor up")
  def rotorPush(self, vizController): print("rotor push")


### end ###
