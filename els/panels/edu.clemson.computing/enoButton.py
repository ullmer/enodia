# Enodia Button-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# Brygg Ullmer, Clemson University
# Begun 2022-02-22

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from pygame import Rect

##################### pygamezero button #####################

class enoButton:
  basePos    = (0,0)
  offsetPos  = (100, 30)
  #offsetPos  = (190, 30)
  buttonRect = None
  buttonText = ""
  bgcolor1   = (0, 0, 130)
  bgcolor2   = (50, 50, 250)
  fgcolor    = "#bbbbbb"
  alpha      = .8
  fontSize   = 48

  toggleMode  = True
  toggleState = False

  ############# constructor #############

  def __init__(self, buttonText, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.buttonText = buttonText
    self.buttonRect = Rect(self.basePos, self.offsetPos)

  ############# pgzero draw #############

  def draw(self, screen):
    if self.toggleMode and self.toggleState: bgcolor = self.bgcolor2
    else:                                    bgcolor = self.bgcolor1

    screen.draw.filled_rect(self.buttonRect, bgcolor)
    screen.draw.text(self.buttonText, self.basePos, 
                     fontsize=self.fontSize, color=self.fgcolor, alpha=self.alpha)

  ############# nudge #############

  def nudgeY(self, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.offsetPos)

  def nudgeXY(self, dx, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx+dx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.offsetPos)

  ######################### on_mouse_down #########################

  def toggle(self):
    if self.toggleState: self.toggleState = False
    else:                self.toggleState = True

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    if self.buttonRect.collidepoint(pos): 
      print(self.buttonText, "pressed")
      self.toggle()
      return True

    return False

##################### pygamezero button #####################

class enoButtonArray:
  basePos = (0,0)
  #dx, dy  = 190, 40
  dx, dy  = 190, 0

  textArray    = None
  buttonArray  = []
  lastSelected = None

  ############# constructor #############

  def __init__(self, buttonTextList): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.textArray  = buttonTextList
    self.buttonArray = []

    idx = 0
    for text in self.textArray:
      #but = enoButton(text); but.nudgeXY(idx*self.dx, idx*self.dy)
      but = enoButton(text, basePos = (idx*self.dx, idx*self.dy))
      self.buttonArray.append(but); idx += 1

  ############# pgzero draw #############

  def draw(self, screen): 
    for but in self.buttonArray: but.draw(screen)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    for but in self.buttonArray:
      if but.on_mouse_down(pos):
        if self.lastSelected is not None: self.lastSelected.toggle()
        self.lastSelected = but

### end ###
