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

class np2DCharArr: #
  arr         = None
  shape       = None
  defaultChar = None
  verbose     = False
  colormap    = {'O': (255, 128, 0), 'P': (128, 0, 128), 
    'R': (255, 0, 0), 'W': (255, 255, 255), 'G': (0, 255, 0),
    'B': (0, 0, 255)}

  ############## constructor ############## 

  def __init__(self, shape=(3,3), defaultChar = '.'):
    self.defaultChar = defaultChar; self.shape = shape
    dcint = ord(defaultChar)
    self.arr = np.full(shape, dcint, dtype=np.uint8)
    # self.buildColormap()
  
  ############## build colormap ############## 
  # def buildColormap(self): 

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
        if j % 2 == 0: i2 = i
        else:          i2 = numRows-i-1
        if self.verbose: print("%i,%i" % (i2, j))

        val = self.arr[i2][j]
        c = '%c' % val
        result += c
    return result
    
############## main #############

if __name__ == '__main__':
  na = np2DCharArr((4,4))
  na.fillRow(1, 'P')
  na.fillCol(1, 'O')
  na.fillRow(3, 'P')
  na.print()
  print("\n" + na.genColWeave())

### end ###
