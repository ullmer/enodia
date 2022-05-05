# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-01

import yaml, sys, traceback

###################################################################
####################### Enodia Spread Panel ####################### 

class enoSpread:

  spreadName, spreadYFn, spreadYF, spreadY, spreadEls = [None] * 5
  imgDirX1, imgDirX6, imgDirD6                        = [None] * 3

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
  es = enoSpreads()
    
### end ###
