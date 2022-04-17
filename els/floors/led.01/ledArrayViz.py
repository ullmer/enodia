# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

import ledArray

############## numpy|ulab 2D character array #############

class ledArrayViz: 
  ledArrayHandle   = None
  rectList         = None
  vertList         = None
  rectDim          = (3,3)
  basePos          = (50, 50)
  dx, dy           = 30, 30
  defaultRectColor = (20, 20, 20)

  ############## constructor ##############

  def __init__(self, ledArray):
    self.ledArrayHandle = ledArray
    self.constructGridViz()

  ############## construct rects ##############

  def constructGridViz(self):
    rows, cols = self.ledArrayHandle.getShape()
    self.vertList = []

    cy = self.basePos[1]

    for i in rows:
      cx = self.basePos[0]
      for j in cols:
        vert = (cx, cy)
        self.vertList.append(vert)
        cx += self.dx
      cy += self.dy

    self.constructRects(self.vertList)

  ############## construct rects ##############

  def constructRects(self, vertList):
    self.rectList = []

    for vert in vertList:
      rect = Rect(rectPos, self.rectDim)
      self.rectList.append(rect)

  ############## draw rects ##############

  def drawRects(self, screen):
    for rect in self.rectList:
      screen.draw.filled_rect(rect, self.defaultRectColor)

  ############# pgzero draw #############

  def draw(self, screen):
    self.drawRects(screen)
    
############## main #############

if __name__ == '__main__':

  ### drawGrid ###
  na = np2DCharArr((4,4))
  na.fillRow(1, 'P')
  na.fillCol(1, 'O')
  na.fillRow(3, 'P')

  global lav
  lav = self.ledArrayViz(na)
  
global lav

def draw(): 
   global screen, lav
   lav.draw(screen)

### end ###
