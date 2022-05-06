# SC example
# Brygg Ullmer, Clemson University
# Begun 2022-04-28
 
WIDTH, HEIGHT = 1280, 1280

baseImgFn   = "ipanel-sc34c"


################### touchlight class ################### 

class touchlight:
  highlightFn = "red-hl-1in-200dpi"
  centerPos   = None
  pgzactor    = None
  dpi         = 200

  def __init__(self, center=(100,100)):
    self.centerPos = center
    self.pgzactor = Actor(self.highlightFn, center=self.centerPos)

  def draw(self): self.pgzactor.draw()

  def setPosIn(self, xin, yin): 
     x = (int)(1.0 * xin * self.dpi)
     y = (int)(1.0 * yin * self.dpi)
     self.centerPos = (x, y)
     self.pgzactor.center = self.centerPos

################### touchlight class ################### 

scMap      = Actor(baseImgFn)
tl1 = touchlight((100, 100))
tl2 = touchlight((100, 400))

tl1.setPosIn(1.218, 1.596)
tl2.setPosIn(1.218, 2.901)

drawList = [scMap, tl1, tl2]

def draw():
  global scMap, tl1, tl2, drawList
  for drawEl in drawList: drawEl.draw()
  

#def update():
#  draw()

### end ###
