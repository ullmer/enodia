# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

import ledArray

############## numpy|ulab 2D character array #############

class ledArrayViz: 
  ledArrayHandle   = None
  rectList         = None
  rectDim          = (3,3)
  defaultRectColor = (20, 20, 20)

  ############## constructor ##############

  def __init__(self, ledArray):
    self.ledArrayHandle = ledArray

  ############## construct rects ##############

  def constructRects(self, vertList):
    self.rectList = []

    for vert in vertList:
      rect = Rect(rectPos, self.rectDim)
      self.rectList.append(rect)

  ############## draw rects ##############

  def drawRects(self):
    for rect in self.rectList:
      screen.draw.filled_rect(rect, self.defaultRectColor)

  ############# pgzero draw #############

  def draw(self, screen):
    self.drawRects()
    
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
