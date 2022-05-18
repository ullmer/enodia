# Simple digits library
# Brygg Ullmer, Clemson University
# Begun 2022-05-18

class enoDigits:
  directory       = 'num-lob/'
  digitActors     = None #individual digits: 0, 1, ...
  digitWidths     = None
  numberPositions = None #potentially multi-digit numbers
 
  x, y  = 100, 100

  ##################### initialize #####################

  def __init__(self):
    self.loadDigits()

  ##################### load digits #####################

  def loadDigits(self):
    self.digitActors     = {}
    self.digitWidths     = {}
    self.numberPositions = {}

    for i in range(9):
      fn = self.directory + i
      a  = Actor(fn)

      self.digitActors[i] = a
      self.digitWidths[i] = a

  ##################### draw digits #####################

  def drawDigits(self, digits):
    if self.digitActors == None: print("enoDigits not initialized!"); return None

    result = []

### end ###
