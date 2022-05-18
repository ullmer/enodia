# Simple digits library
# Brygg Ullmer, Clemson University
# Begun 2022-05-18

class enoDigits:
  directory   = 'num-lob/'
  digitActors = None
 
  x, y  = 100, 100

  ##################### initialize #####################

  def __init__(self):
    self.loadDigits()

  ##################### load digits #####################

  def loadDigits(self):
    self.digitActors = {}

    for i in range(9):
      fn = self.directory + i
      a  = Actor(fn)
      self.digitActors[i] = a

### end ###
