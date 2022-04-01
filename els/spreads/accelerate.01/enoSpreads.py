# Enodia spreads // touchscreen class
# Brygg Ullmer, Clemson University
# Begun 2022-04-01

import yaml

####################### Enodia Spreads ####################### 

class enoSpreads:
  spreadsYFn = "yaml/spreads.yaml"
  spreadsYF  = None
  spreadsY   = None

  ####################### constructor ####################### 
  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml()
    
  ####################### load YAML ####################### 
  def loadYaml(self):

    try:
      self.spreadsYF = open(self.spreadsYFn, "r+t")
      self.spreadsY = yaml.safe_load(self.spreadsYF)
    except: print("enoSpreads loadYaml: caught error")

    print(self.spreadsY)

####################### Enodia Spread ####################### 

class enoSpread:
  pass

####################### main ####################### 

if __name__ == '__main__': 
  es = enoSpreads()

### end ###
