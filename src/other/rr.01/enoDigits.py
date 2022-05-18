# Simple digits library
# Brygg Ullmer, Clemson University
# Begun 2022-05-18

class enoDigits:
  font            = "LobsterTwo-Regular"
  numbers         = None 
  numberPositions = None 
  nextNumberId    = 0
  screen          = None 

  directory       = 'num-lob/'
  digitActors     = None #individual digits: 0, 1, ...
  digitWidths     = None

  ##################### initialize #####################

  def __init__(self, screen):
    self.screen          = screen
    self.numbers         = {}
    self.numberPositions = {}

    #self.loadDigits() 

  ##################### initialize #####################

  def introduceNumber(self, whichNum, whichPos):
    numId = self.nextNumberId
    self.numbers[numId]         = whichNum
    self.numberPositions[numId] = whichPos
    self.nextNumberId += 1

  ##################### initialize #####################

  def drawNumbers(self):
    numIds = self.numbers.keys()

    for numId in numIds:
      whichNum = self.numbers[numId]
      whichPos = self.numberPositions[numId] 

      self.screen.draw.text(whichNum, whichPos, fontname = self.font)

  ##################### load digits #####################

  def loadDigits(self):  #initial image-based approach; shelved for the moment
    self.digitActors     = {}
    self.digitWidths     = {}
    self.numberPositions = {}

    for i in range(9):
      fn = self.directory + i
      a  = Actor(fn)

      self.digitActors[i] = a
      self.digitWidths[i] = a

  ##################### draw digits #####################

  def drawDigits(self, digits): #initial imag-ebased approach; shelved for the moment
    if self.digitActors == None: print("enoDigits not initialized!"); return None
    result = []

### end ###
