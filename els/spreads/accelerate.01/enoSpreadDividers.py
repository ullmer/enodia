# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-01

import yaml, sys, traceback

###################################################################
####################### Enodia Spread Panel ####################### 

class enoSpreadDividers:

  dhandle  = "divider01"
  yamlFn   = "yaml/divider01.yaml"
  yamlF    = None

  dividerY         = None
  dividerPdfPrefix = None
  dividerFnHash    = None

  ####################### constructor ####################### 

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml()
    #for t in [1,2]: self.enoActorLTiered[t] = []

  ####################### warn message ####################### 

  def warn(self, msg):
    try: print("enoSpreadDividers warning:", msg)
    except: pass

  ####################### load YAML ####################### 

  def loadYaml(self):
    try:
      self.warn("loadYaml calling open + safe_load on " + self.spreadYFn)
      self.yamlF = open(self.yamlFn, "rt")
      self.dividerY = yaml.safe_load(self.yamlF)
    except: self.warn("loadYaml: caught error"); traceback.print_exc()

    if self.verbose: self.warn(self.dividerY)

    try:
      y = self.dividerY
      yp  = y["panel"]
      yph = yp["handle"]
      if yph != self.dhandle: 
        self.warn("loadYaml: panel does not match specified handle"); return None

      ypid   = yp["imgDir"]
      ypipre = yp["imgPrefix"]
      ypiext = yp["imgExt"]
      ypels  = yp["els"]
      ypidb  = ypid["base"]
      ypeup  = ypels["upper"]
      ypelo  = ypels["lower"]

      self.dividerPdfPrefix = ypidb + ypipre
      self.dividerFnHash    = {}
       
      for el in ypeup + ypelo: #synthesis of both lists



      

####################### main ####################### 

if __name__ == '__main__': 
  esd = enoSpreadDividers()
    
### end ###


  els:
    upper: [U1, U2, U3]
    lower: [L1, L2, L3]
