# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

import ledArray

############## numpy|ulab 2D character array #############

class ledArrayViz: 
  ledArrayHandle = None

  ############## constructor ##############

  def __init__(self, ledArray):
    self.ledArrayHandle = ledArray

  ############## draw grid ##############

  def draw(self):
    
############## main #############

if __name__ == '__main__':

  ### drawGrid ###
  na = np2DCharArr((4,4))
  na.fillRow(1, 'P')
  na.fillCol(1, 'O')
  na.fillRow(3, 'P')



### end ###
