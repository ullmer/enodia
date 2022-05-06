# Enodia spreads dividers class
# Brygg Ullmer, Clemson University
# Begun 2022-05-05

# Probably should have implemented far more simply initially, but
# keep targeting prospects for generalizing...

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
      if self.verbose: print(y)
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
        if self.verbose: print(el, self.dividerFnHash[el])
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
    key = tb + str(idx+1)
    if self.verbose: print("key:", key)
    result = self.getFnKey(key)
    return result

 ####################### getFn ####################### 

  def getFnIdx(self, idx, numCols=3):
    if idx < 3: result = self.getFnCoord('U', idx)
    else:       result = self.getFnCoord('L', idx-numCols) #numCols somewhat problematic
    return result

####################### main ####################### 

if __name__ == '__main__': 
  esd = enoSpreadDividers()
  for i in range(6):
    fn = esd.getFnIdx(i)
    print("fn:", fn)
    
### end ###

