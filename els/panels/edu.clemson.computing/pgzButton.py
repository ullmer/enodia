# Button-like elements for Pygame Zero
# Brygg Ullmer, Clemson University
# Begun 2022-02-22

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from pygame import Rect

##################### pygamezero button #####################

class pgzButton:
  basePos    = (0,0)
  offsetPos  = (100, 30)
  #offsetPos  = (190, 30)
  buttonRect = None
  buttonText = ""
  bgcolor    = (0, 0, 130)
  fgcolor    = "#bbbbbb"
  alpha      = .8
  fontSize   = 48

  toggleMode  = True
  toggleState = False

  def __init__(self, buttonText): 
    self.buttonText = buttonText
    self.buttonRect = Rect(self.basePos, self.offsetPos)

  def draw(self, screen): 
    screen.draw.filled_rect(self.buttonRect, self.bgcolor)
    screen.draw.text(self.buttonText, self.basePos, 
                     fontsize=self.fontSize, color=self.fgcolor, alpha=self.alpha)

  def nudgeY(self, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.offsetPos)

  def nudgeXY(self, dx, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx+dx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.offsetPos)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    if self.buttonRect.collidepoint(pos): print(self.buttonText, " pressed")

##################### pygamezero button #####################

class pgzButtonArray:
  basePos = (0,0)
  #dx, dy  = 190, 40
  dx, dy  = 190, 0

  textArray   = None
  buttonArray = []

  def __init__(self, buttonTextList): 
    self.textArray  = buttonTextList
    self.buttonArray = []

    idx = 0
    for text in self.textArray:
      but = pgzButton(text); but.nudgeXY(idx*self.dx, idx*self.dy)
      self.buttonArray.append(but); idx += 1

  def draw(self, screen): 
    for but in self.buttonArray: but.draw(screen)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    for but in self.buttonArray:
      but.on_mouse_down(pos)

### end ###
