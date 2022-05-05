# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-01

import yaml, sys, traceback

###################################################################
####################### Enodia Spread Panel ####################### 

class enoSpreadDividers:

  yamlFn  = "yaml/divider01.yaml"
  dhandle = "divider01"

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
    self.projActorCache  = {}

    for t in [1,2]: self.enoActorLTiered[t] = []

    self.loadYaml(spreadName)
    self.parseTouchElsY()
    self.cacheColorbars()

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

####################### main ####################### 

if __name__ == '__main__': 
  esd = enoSpreadDividers()
    
### end ###


panel:
  handle: divider01 #panel dividers on spreads
  name:   Panel Divider 01

  imgDir:
    x1: acc_bc/x1/ #100dpi  #for screen animations during rolling, it's
    x6: acc_bc/x6/ #600dpi  #possible that we may wish pixel/image versions
    d6: acc_bc/d6/ #100/6 dpi

# images/dividers/x1 : rollDividerCU02e_L2.pdf  rollDividerCU02e_U1.pdf

  imgPrefix:       "rollDividerCU02e_"
  imgExt:          ".png"

  els:
    upper: [U1, U2, U3]
    lower: [L1, L2, L3]

