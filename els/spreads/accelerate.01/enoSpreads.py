# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-01

import yaml, sys, traceback

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
  SpreadEls  = None

  spreadTouchEls = None

  ####################### constructor ####################### 

  def __init__(self, spreadName, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml(spreadName)

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
      self.spreadEls = self.spreadY["panel"]["els"] # later, should handle plurality of panels
      for el in self.spreadEls: 
        abbrev = el["abbrev"]; name = el["name"]
        self.constructTouchEl
    except: print("enoSpread loadYaml: caught error"); traceback.print_exc()
  
####################### main ####################### 

if __name__ == '__main__': 
  es = enoSpreads()

### end ###
