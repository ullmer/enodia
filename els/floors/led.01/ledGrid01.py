# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

from ledArray import *

na = np2DCharArr((10,10))

for i in range(3):
  na.fillRow(i*3, 'P')
  na.fillCol(i*3, 'P')

na.print()
weaveCh = na.genColWeave()
weaveCo = na.mapColorStr2Int(weaveCh)
print("\n" + weaveCh)
print("\n" + str(weaveCo))

### end ###
