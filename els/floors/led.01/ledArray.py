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

class np2DChAr: #
  arr         = None
  shape       = None
  defaultChar = None

  def __init__(shape=(3,3), defaultChar = '.'):
    self.defaultChar = defaultChar; self.shape = shape
    dcint = ord(defaultChar)
    self.arr = np.full(shape, dcint, dtype=np.uint8)
    
############## main #############

np2dca = np2DChAr()

### end ###
