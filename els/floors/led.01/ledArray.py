# Library support for 2D LED strip arrays
# By Brygg Ullmer and Sida Dai, Clemson University
# Begun 2022-04-13

try: #https://github.com/v923z/micropython-ulab
    from ulab import numpy as np
    from ulab import scipy as sp

except ImportError:
    import numpy as np
    import scipy.special

#a = numpy.full((3,3), '.', dtype=numpy.char)

############## numpy|ulab 2D character array #############

class np2DCharArr: #
  arr         = None
  shape       = None
  defaultChar = None

  ############## constructor ############## 

  def __init__(self, shape=(3,3), defaultChar = '.'):
    self.defaultChar P= defaultChar; self.shape = shape
    dcint = ord(defaultChar)
    self.arr = np.full(shape, dcint, dtype=np.uint8)
  
  ############## fill row ############## 
  
  def fillRow(self, whichRow, whichChar):
    wcint = ord(whichChar)
    maxIdx = shape[0]
    for i in range(maxIdx): self.arr[whichRow][i] = wcint

  ############## print ############## 

  def print(self):
    #https://numpy.org/doc/stable/reference/generated/numpy.array2string.html
    s = np.array2string(self.arr, separator='', formatter={'int':lambda x: chr(x)}) 
    print(s)
    
############## main #############

na = np2DCharArr((8,8))
na.print()

### end ###
