# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

try: #https://github.com/v923z/micropython-ulab
    from ulab import numpy as np
    from ulab import scipy as sp

except ImportError:
    import numpy as np
    import scipy.special

#a = numpy.full((3,3), '.', dtype=numpy.char)

############## numpy|ulab 2D character array #############

class ledArrayViz: 
  ledMap = None


  ############## constructor ##############

  def __init__(self, shape=(3,3), defaultChar = '.'):
    self.ledMap = np2DCharArr(shape, defaultChar)

  ############## draw grid ##############

  def drawGrid(self):
    self.ledMap.fillRow(1, 'P')
    self.ledMap.fillCol(1, 'O')
    self.ledMap.fillRow(3, 'P')
    self.ledMap..print()
    weaveCh = na.genColWeave()
    weaveCo = na.mapColorStr2Int(weaveCh)
    print("\n" + weaveCh)
    print("\n" + str(weaveCo))
    
############## main #############

if __name__ == '__main__':

### drawGrid ###
  na = np2DCharArr((4,4))
  na.fillRow(1, 'P')
  na.fillCol(1, 'O')
  na.fillRow(3, 'P')
  na.print()
  weaveCh = na.genColWeave()
  weaveCo = na.mapColorStr2Int(weaveCh)
  print("\n" + weaveCh)
  print("\n" + str(weaveCo))

### end ###
