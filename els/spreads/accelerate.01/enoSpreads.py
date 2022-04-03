# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-01

import yaml, sys, traceback
from enoActor import *

##############################################################
####################### Enodia Spreads ####################### 

class enoSpreads:
  spreadsYFn = "yaml/spreads.yaml"
  spreadsYF  = None
  spreadsY   = None
  spreadsYL  = None
  spreadsL   = None

  ####################### constructor ####################### 

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml()
    self.parseYaml()
    
  ####################### load YAML ####################### 

  def loadYaml(self):

    try:
      self.spreadsYF = open(self.spreadsYFn, "r+t")
      self.spreadsY = yaml.safe_load(self.spreadsYF)
    except: print("enoSpreads loadYaml: caught error")

    print(self.spreadsY)
  
  ####################### parse YAML ####################### 

  def parseYaml(self):

    if self.spreadsY == None:
      print("enoSpreads parseYaml: no YAML struct found"); return -1

    self.spreadsL = []
    try:    
      self.spreadsYL = self.spreadsY["spreads"]  #list of spreads
      for spreadName in self.spreadsYL:
        newSpread = enoSpread(spreadName)
        self.spreadsL.append(newSpread)

    except: print("enoSpreads parseYaml: problems parsing YAML"); traceback.print_exc()

#############################################################
####################### Enodia Spread Panel ####################### 

#class enoSpreadPanel:
class enoSpread:
  spreadName = None
  spreadYFn  = None
  spreadYF   = None
  spreadY    = None
  spreadEls  = None
  imgDir1, imgDir6 = None, None
  imgPrefix, imgExt, imgPostfixTouch, imgPostfixFull = [None] * 4
  tiers, tierPosOff, dim, pos                        = [None] * 4
  elPosCache = None
  verbose    = False

  spreadTouchEls = None

  ####################### constructor ####################### 

  def __init__(self, spreadName, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.elPosCache = {}

    self.loadYaml(spreadName)
    self.parseTouchElsY()

  ####################### load YAML ####################### 

  def loadYaml(self, spreadName):
    self.spreadName = spreadName
    self.spreadYFn = "yaml/" + self.spreadName + ".yaml"
    try:
      self.spreadYF = open(self.spreadYFn, "r+t")
      self.spreadY = yaml.safe_load(self.spreadYF)
    except: print("enoSpread loadYaml: caught error"); traceback.print_exc()

    print(self.spreadY)

  #################### parse touch elements from yaml ###################

  def parseTouchElsY(self):
    try:
      panel          = self.spreadY["panel"]
      self.imgDir1   = panel["imgDir"]["d1"]
      self.imgDir6   = panel["imgDir"]["d6"]
      self.imgPrefix = panel["imgPrefix"]
      self.imgExt    = panel["imgExt"]

      self.imgPostfixTouch = panel["imgPostfixTouch"]
      self.imgPostfixFull  = panel["imgPostfixFull"]

      self.dim             = panel["dim"]
      self.pos             = panel["pos"]

      self.tiers           = panel["tiers"]
      self.tierPosOff      = panel["tierPosOff"]
      self.spreadEls       = panel["els"] 
      # later, should handle plurality of panels

      for el in self.spreadEls: 
        abbrev = el["abbrev"]; name = el["name"]
        ifn = self.imgDir1 + self.imgPrefix + \
              abbrev + self.imgPostfixTouch + self.imgExt
        self.constructTouchEl(abbrev, name, ifn)

    except: print("enoSpread loadYaml: caught error"); traceback.print_exc()

  #################### calcTouchElPos ###################

  def getTouchElPos(self, elAbbrev):
    if elAbbrev in self.elPosCache: return self.elPosCache[elAbbrev]

    whichTier = None

    try:
      for tier in self.tiers.keys():
        if elAbbrev in self.tiers[tier]: whichTier = tier

      if whichTier is None: 
        print("enoSpread calcTouchElPos: whichTier none"); return -1

      tierEls = self.tiers[whichTier]
      elIdx   = tierEls.index(elAbbrev)

      tierPos = self.tierPosOff[whichTier]["pos"]
      tierOff = self.tierPosOff[whichTier]["dxy"]

      if self.verbose: print("tp, to:", tierPos, tierOff)

      tpx, tpy = tierPos[0], tierPos[1]
      tdx, tdy = tierOff[0], tierOff[1]

      x = tpx + tdx * elIdx
      y = tpy + tdy * elIdx

      elPos = (x, y)
      self.elPosCache[elAbbrev] = elPos 
      return elPos
      #so that we don't have to recalculate, in base case of non-movings els

    except: 
      print("enoSpread calcTouchElPos: caught error"); traceback.print_exc()
      print("elAbbrev:", elAbbrev)
  
  #################### constructTouchEl ###################

  def constructTouchEl(self, abbrev, name, imgFn):
    elPos = self.getTouchElPos(abbrev)
    print("enoSpread constructTouchEl:", abbrev, name, imgFn, elPos)

    ete = enoActor(imgFn, abbrev=abbrev)

####################### main ####################### 

if __name__ == '__main__': 
  es = enoSpreads()

### end ###
