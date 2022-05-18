# Animated numbers library
# Brygg Ullmer, Clemson University
# Begun 2022-05-18
  
##################### enodia numbers #####################

class enoNumbers:
  font            = "lobstertwo-regular"
  fontsize        = 40
  numbers         = None 
  numberPositions = None 
  nextNumberId    = 0
  screen          = None 
  bubbleRadius    = 30     # bubble radius
  bubbleColor     = (50, 50, 50)

  directory       = 'num-lob/'
  digitActors     = None #individual digits: 0, 1, ...
  digitWidths     = None

  ##################### initialize #####################

  def __init__(self, screen):
    self.screen          = screen
    self.numbers         = {}
    self.numberPositions = {}

    #self.loadDigits() 

  ##################### introduce numbers #####################

  def introduceNumber(self, whichNum, whichPos):
    numId = self.nextNumberId
    self.numbers[numId]         = whichNum
    self.numberPositions[numId] = whichPos
    self.nextNumberId += 1

  ##################### draw numbers #####################

  def drawNumbers(self):
    numIds = self.numbers.keys()

    for numId in numIds:
      whichNum = self.numbers[numId]
      whichPos = self.numberPositions[numId] 

      self.screen.draw.text(str(whichNum), center = whichPos, fontname = self.font, 
        fontsize = self.fontsize)

  ##################### initialize #####################

  def drawBubbledNumbers(self):
    numIds = self.numbers.keys()

    for numId in numIds:
      whichPos = self.numberPositions[numId] 
      self.screen.draw.filled_circle(whichPos, self.bubbleRadius, self.bubbleColor)

    self.drawNumbers()


##################### enodia animated numbers #####################

class enoAnimNumbers(enoNumbers):

  ##################### initialize #####################

  def __init__(self, screen):
    super().__init__(screen) 

### end ###
