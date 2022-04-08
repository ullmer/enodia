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
      self.spreadsYF = open(self.spreadsYFn, "rt")
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

###################################################################
####################### Enodia Spread Panel ####################### 

#class enoSpreadPanel:

class enoSpread:

  spreadName, spreadYFn, spreadYF, spreadY, spreadEls = [None] * 5
  imgDirX1, imgDirX6, imgDirD6                        = [None] * 3
  imgPrefix, imgExt, imgPostfixTouch, imgPostfixFull  = [None] * 4
  tiers, tierPosOff, tierPosShim, dim, pos, elPosCache= [None] * 6
  enoActorL, spreadTouchEls                           = [None] * 2
  touchEl2Tier, enoActorLTiered, abbrevL              = [None] * 3
  selectedTouchEl, abbrev2enoActor, projActors        = [None] * 3
  cursorActor, cursorPos, enoActorLarge               = [None] * 3
  lastLarge, currentLarge, colorBars, colorbarL       = [None] * 4
  cursorImgFn                                         = "x1/cursor1"
  tween = 'accel_decel'
  animDuration = .7

  #touchElBasePos, touchElDxDy                        = [None] * 2

  firstDraw  = True
  verbose    = False
  cursorDy   = -36
  enoActorLargeHiddenPos   = (50, 850)
  enoActorLargeVisiblePos  = (50, 100)
  enoActorLargeDepartedPos = (50, -850)
  enoActorLargeDy          = 200

  spreadTouchEls = None

  ####################### constructor ####################### 

  def __init__(self, spreadName, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.enoActorL    = []
    self.abbrevL      = []
    self.colorbarL    = []
    self.projActors   = []
    self.elPosCache      = {}
    self.touchEl2Tier    = {}
    self.enoActorLTiered = {}
    self.enoActorLarge   = {}
    self.abbrev2enoActor = {}

    for t in [1,2]: self.enoActorLTiered[t] = []

    self.loadYaml(spreadName)
    self.parseTouchElsY()
    self.cacheColorbars()

  ####################### get colorbar info #######################

  def cacheColorbars(self):
    self.colorbarL = []
    try:
      for cb in self.colorBars:
        for abbrev in cb:
          color  = cb[abbrev]
          self.colorbarL.append(color)
    except: pass

  ####################### get colorbar info #######################

  def getColorbarInfo(self):
    #print(self.colorBars)
    print(self.colorbarL)
  
  ####################### get colorbar info #######################

  def getColorBarL(self):
    return self.colorbarL

  def getColorBarN(self, n):
    return self.colorbarL[n]

  ####################### build cursor #######################

  def buildCursor(self, preferredStarterAbbrev = None):
    targAbbrev = None

    if self.cursorPos is None:
      if preferredStarterAbbrev is not None:
        if preferredStarterAbbrev in self.abbrevL:
          targAbbrev = preferredStarterAbbrev
      elif self.abbrevL is not None and len(self.abbrevL) > 0: targAbbrev = self.abbrevL[0]     
      self.cursorPos = self.getTouchElPos(targAbbrev)

    if self.cursorActor is None:
      cpos = self.cursorPos

      if targAbbrev in self.touchEl2Tier and \
         self.touchEl2Tier[targAbbrev] == 2: 
        cpos = (cpos[0], cpos[1] + self.cursorDy)

      self.cursorActor = Actor(self.cursorImgFn, center=cpos)

  ####################### move cursor #######################
  
  def moveCursor(self, targetAbbrev):
    self.cursorPos = self.getTouchElPos(targetAbbrev)
    cpos = self.cursorPos

    if targetAbbrev in self.touchEl2Tier and \
      self.touchEl2Tier[targetAbbrev] == 2: 
      cpos = (cpos[0], cpos[1] + self.cursorDy)

    animate(self.cursorActor, center=cpos, \
            tween=self.tween, duration=self.animDuration)

  ####################### warn #######################

  def warn(self, msg):
    try: print("enoSpread warning:", msg)
    except: pass

  ####################### showLarge #######################

  def showLarge(self, abbrev):
    posShim = self.tierPosShim

    hpos = self.enoActorLargeHiddenPos
    vpos = self.enoActorLargeVisiblePos

    hpos2 = (hpos[0]+posShim[0], hpos[1]+posShim[1])

    if abbrev in self.enoActorLarge:
      eal = self.enoActorLarge[abbrev]
    else: 
      ifn = self.imgDirX6 + self.imgPrefix + abbrev + self.imgPostfixTouch
      eal = self.enoActorLarge[abbrev] = Actor(ifn, pos=hpos2)

    if abbrev in self.touchEl2Tier and \
       self.touchEl2Tier[abbrev] == 2: 
      #vpos = (vpos[0], vpos[1] + self.enoActorLargeDy)
      vpos = (vpos[0] + posShim[0], vpos[1] + posShim[1] + self.enoActorLargeDy)

    self.lastLarge = self.currentLarge

    if self.lastLarge is not None:
      vpos2 = self.enoActorLargeDepartedPos
      vpos3 = (vpos2[0] + posShim[0], vpos2[1] + posShim[1])
      animate(eal, center=vpos3, tween=self.tween, duration=self.animDuration)

    animate(eal, center=vpos, tween=self.tween, duration=self.animDuration)

    self.currentLarge = eal

  ####################### load YAML ####################### 

  def loadYaml(self, spreadName):
    self.spreadName = spreadName
    self.spreadYFn = "yaml/" + self.spreadName + ".yaml"
    try:
      self.warn("loadYaml calling open + safe_load on " + self.spreadYFn)
      self.spreadYF = open(self.spreadYFn, "rt")
      self.spreadY = yaml.safe_load(self.spreadYF)
    except: self.warn("loadYaml: caught error"); traceback.print_exc()

    if self.verbose: self.warn(self.spreadY)

  #################### parse touch elements from yaml ###################

  def parseTouchElsY(self):
    try:
      panel          = self.spreadY["panel"]
      self.imgDirX1  = panel["imgDir"]["x1"]
      self.imgDirX6  = panel["imgDir"]["x6"]
      self.imgDirD6  = panel["imgDir"]["d6"]
      self.imgPrefix = panel["imgPrefix"]
      self.imgExt    = panel["imgExt"]

      self.imgPostfixTouch = panel["imgPostfixTouch"]
      self.imgPostfixFull  = panel["imgPostfixFull"]

      #self.touchElBasePos  = panel["touchElBasePos"]
      #self.touchElDxDy     = panel["touchElDxDy"]

      self.dim             = panel["dim"]
      self.pos             = panel["pos"]

      self.colorBars       = self.spreadY["colorBars"]

      self.tiers           = panel["tiers"]
      self.tierPosShim     = panel["tierPosShim"]
      self.tierPosOff      = panel["tierPosOff"]
      self.spreadEls       = panel["els"] # later, should handle plurality of panels

      for el in self.spreadEls: 
        abbrev = el["abbrev"]; name = el["name"]

        #ifn = self.imgDirX1 + self.imgPrefix + \
        #      abbrev + self.imgPostfixTouch + self.imgExt

        ifn = self.imgDirX1 + self.imgPrefix + \
              abbrev + self.imgPostfixTouch 
        self.constructTouchEl(abbrev, name, ifn)
        self.abbrevL.append(abbrev)

      self.setupTouchElTiers() # divide touch elements into tiers 

      self.buildBCtouch()

    except: self.warn("loadYaml: caught error"); traceback.print_exc()

  #################### setup touch element tiers ###################

  def buildBCtouch(self):
    x=0; y=0; dx = 600
    for u in ["bc2", "cu2"]:
      self.constructTouchEl2(u, '', 'acc_bc/x1/'+u, (x,y))
      x += dx

  #################### setup touch element tiers ###################

  def setupTouchElTiers(self):
    for abbrev in self.abbrevL:
      foo  = self.getTouchElPos(abbrev) # hack to ensure touchEl2Tier populated
      tier = self.touchEl2Tier[abbrev] 
      self.enoActorLTiered[tier].append(abbrev)

  #################### calcTouchElPos ###################

  def getTouchElPos(self, elAbbrev):
    if elAbbrev is None: return (0, 0) 
    if elAbbrev in self.elPosCache: return self.elPosCache[elAbbrev]

    whichTier = None

    try:
      for tier in self.tiers.keys():
        if elAbbrev in self.tiers[tier]: whichTier = tier

      if whichTier is None: 
        self.warn("calcTouchElPos: whichTier none"); return -1

      self.touchEl2Tier[elAbbrev] = whichTier

      tierEls = self.tiers[whichTier]
      elIdx   = tierEls.index(elAbbrev)

      tierPos = self.tierPosOff[whichTier]["pos"]
      tierOff = self.tierPosOff[whichTier]["dxy"]
      tierPosShim = self.tierPosShim

      if self.verbose: self.warn("tp, to:", tierPos, tierOff)

      tpx, tpy = tierPos[0], tierPos[1]
      tdx, tdy = tierOff[0], tierOff[1]
      tps = tierPosShim

      x = tpx + tps[0] + tdx * elIdx
      y = tpy + tps[1] + tdy * elIdx

      elPos = (x, y)
      self.elPosCache[elAbbrev] = elPos 
      return elPos
      #so that we don't have to recalculate, in base case of non-movings els

    except: 
      self.warn("calcTouchElPos: caught error"); traceback.print_exc()
      self.warn("elAbbrev:", elAbbrev)
  
  #################### draw ###################

  def draw(self, vizController):
    if self.enoActorL is None:
      self.warn("draw: enoActorL is empty"); return

    if self.firstDraw: self.buildCursor(); self.firstDraw=False

    idx = 0; thresh = 5

    colorbarPos = 50; cbDx = 600
    for i in range(3):
      color = self.getColorBarN(i)
      vizController.drawTranspColorbar(color, colorbarPos)
      colorbarPos += cbDx

    vizController.drawTranspOverlayLower(self.tierPosShim)
    #self.getColorbarInfo()

    selectedEte = None

    tier1ActorAbbrevs = self.enoActorLTiered[1]
    tier2ActorAbbrevs = self.enoActorLTiered[2]

    for tieredActorL in [tier1ActorAbbrevs, tier2ActorAbbrevs]:
      for abbrev in tieredActorL:
        ete = self.abbrev2enoActor[abbrev]
        if ete.getAbbrev() is not self.selectedTouchEl: ete.draw()
        else: selectedEte = ete

    for a in self.projActors: self.abbrev2enoActor[a].draw() 

    if self.lastLarge is not None:
      self.lastLarge.draw()

    if self.currentLarge is not None:
      self.currentLarge.draw()

    if self.cursorActor is not None:
      self.cursorActor.draw()
 
    if selectedEte is not None: selectedEte.draw()

  ################# mouse down #################

  def on_mouse_down(self, pos):
    if self.enoActorL is None:
      self.warn("on_mouse_down: enoActorL is empty"); return

    tier1ActorAbbrevs = self.enoActorLTiered[1]
    tier2ActorAbbrevs = self.enoActorLTiered[2]

    for a in self.projActors: self.abbrev2enoActor[a].on_mouse_down(pos) 

    for tieredActorL in [tier1ActorAbbrevs, tier2ActorAbbrevs]:
      for abbrev in tieredActorL:
        ete = self.abbrev2enoActor[abbrev]
        selected = ete.on_mouse_down(pos)
        if selected:
          ste = self.selectedTouchEl = ete.getAbbrev()
          self.moveCursor(ste)
          self.showLarge(ste)
          return  #allow for only one selected element

  #################### constructTouchEl ###################

  def constructTouchEl(self, abbrev, name, imgFn):
    elPos = self.getTouchElPos(abbrev)

    print("enoSpread constructTouchEl:", abbrev, name, imgFn, elPos)

    ete = enoActor(imgFn, abbrev=abbrev, basePos=elPos) #ete: enodia touch element
    self.enoActorL.append(ete)
    self.abbrev2enoActor[abbrev] = ete
  
#################### constructTouchEl2 ###################

  def constructTouchEl2(self, abbrev, name, imgFn, elPos):
    print("enoSpread constructTouchEl2:", abbrev, name, imgFn, elPos)

    pa = enoActor(imgFn, abbrev=abbrev, basePos=elPos) #ete: enodia touch element
    self.projActors.append(abbrev)
    self.abbrev2enoActor[abbrev] = pa

####################### main ####################### 

if __name__ == '__main__': 
  es = enoSpreads()

### end ###
