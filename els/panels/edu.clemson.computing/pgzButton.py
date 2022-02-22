# Button-like elements for Pygame Zero
# Brygg Ullmer, Clemson University
# Begun 2022-02-22

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/


class pgzButton:
  basePos    = (0,0)
  offsetPos  = (180, 30)
  buttonRect = None
  buttonText = ""
  bgcolor    = (0, 0, 130)
  fgcolor    = "#bbbbbb"
  alpha      = .8
  fontSize   = 48

  def __init__(self, buttonText): 
    self.buttonText = buttonText
    self.buttonRect = Rect(self.basePos, self.offsetPos)

  def draw(): 
    screen.draw.filled_rect(self.buttonRect, self.bgcolor)
    screen.draw.text(self.buttonText, self.basePos, 
                     fontsize=self.fontSize, color=self.fgcolor, alpha=self.alpha)

### end ###
