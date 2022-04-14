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
    self.defaultChar = defaultChar; self.shape = shape
    dcint = ord(defaultChar)
    self.arr = np.full(shape, dcint, dtype=np.uint8)
  
  ############## fill row ############## 
  
  def fillRow(self, whichRow, whichChar):
    wcint = ord(whichChar)
    maxIdx = self.shape[0]
    for i in range(maxIdx): self.arr[whichRow][i] = wcint

  ############## fill col ############## 
  
  def fillCol(self, whichCol, whichChar):
    wcint = ord(whichChar)
    maxIdx = self.shape[1]
    for i in range(maxIdx): self.arr[i][whichCol] = wcint

  ############## print ############## 

  def print(self):
    #https://numpy.org/doc/stable/reference/generated/numpy.array2string.html
    s = np.array2string(self.arr, separator='', formatter={'int':lambda x: chr(x)}) 
    print(s)

  ############## genColWeave ############## 
  
  def genColWeave(self): #generate column-wise "weave," initially for LED chain
    numCols = self.shape[0] 
    numRows = self.shape[1] 
  
    result = ''
    for j in range(numCols):
      for i in range(numRows):
        if j % 2 == 0: j2 = j
        else:          j2 = numCols-j
        print("%i,%i" % (i, j2))

        val = self.arr[i][j2]
        c = '%c' % val
        result += c
    return result
    
############## main #############

if __name__ == '__main__':
  na = np2DCharArr((4,4))
  na.fillRow(1, 'P')
  na.fillCol(1, 'O')
  na.print()
  print(na.genColWeave())

### end ###
