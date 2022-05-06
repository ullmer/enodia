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
  verbose  = False

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
      self.warn("loadYaml calling open + safe_load on " + self.yamlFn)
      self.yamlF = open(self.yamlFn, "rt")
      self.dividerY = yaml.safe_load(self.yamlF)
    except: self.warn("loadYaml: caught error"); traceback.print_exc()

    if self.verbose: self.warn(self.dividerY)

    try:
      y = self.dividerY
      print(y)
      yp  = y["panel"]
      yph = yp["handle"]
      if yph != self.dhandle: 
        self.warn("loadYaml: panel does not match specified handle"); return None

      ypid   = yp["imgDir"]
      ypipre = yp["imgPrefix"]
      ypiext = yp["imgExt"]
      ypels  = yp["els"]
      ypidb  = ypid["base"]
      ypix1  = ypid["x1"]
      ypeup  = ypels["upper"]
      ypelo  = ypels["lower"]

      self.dividerPdfPrefix = ypidb + ypipre
      self.dividerFnHash    = {}
       
      for el in ypeup + ypelo: #synthesis of both lists
        self.dividerFnHash[el] = ypidb + "/" + ypix1 + ypipre + el + ypiext
        print(self.dividerFnHash[el])
    except:
      self.warn("loadYaml error processing data")
      traceback.print_exc()

  ####################### getFn ####################### 

  def getFnKey(self, key):
    if key not in self.dividerFnHash:
      self.warn("getFn references unknown key", key); return None
    result = self.dividerFnHash[key]
    return result
  
 ####################### getFn ####################### 

  def getFnCoord(self, tb, idx):
    key = tb + str(idx)
    result = self.getFnKey(key)
    return result

####################### main ####################### 

if __name__ == '__main__': 
  esd = enoSpreadDividers()
    
### end ###

