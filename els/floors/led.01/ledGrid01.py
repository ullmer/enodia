# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

import os
from ledArray import *

na = np2DCharArr((13,13))

for i in range(4):
  na.fillRow(i*4, 'P')
  na.fillCol(i*4, 'P')

na.clearScr()
na.print()
weaveCh = na.genColWeave()
weaveCo = na.mapColorStr2Int(weaveCh)
print("\n" + weaveCh)
print("\n" + str(weaveCo))

### end ###
