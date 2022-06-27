# Enodia Space/Time operations
# By Brygg Ullmer and Sida Dai, Clemson University
# Begun 2022-06-26

################################################### 
############# Enodia Space base class #############

class EnoSpace:
  spaceStr = None

  ############# constructor  ############# 
  def __init__(self, spaceStr): self.spaceStr = spaceStr

  ############# composite (power) ############# 

  def __pow__(self, other):
    compositeStr = "space %s entangled with space %s" % (
      self.getStr(), other.getStr())

    return compositeStr

  ############# get string ############# 

  def getStr(self): return self.spaceStr 

################################################## 
############# Enodia Time base class #############

class EnoTime:
  timeStr  = None
  beginTime, endTime, currentTime = [None] * 3
  timeUnit = None
  knownTimeUnits = ['zs', 'as', 'fs', 'ps', 'ns', 'us', 'ms', 's', 
        'mn', 'hr', 'dy', 'wk', 'mo', 'yr', 'cn', 'ty', 'my', 'by']

  ############# constructor  ############# 
  def __init__(self, timeStr): self.timeStr = timeStr

  ############# get string ############# 
  def getStr(self): return self.timeStr

################################################## 
########### Enodia Space Time base class #########

class EnoSpaceTime:
  space = None
  time  = None
  
  ############# constructor  ############# 
  def __init__(self, spaceStr, timeStr): 
    self.space = EnoSpace(spaceStr)
    self.time  = EnoSpace(timeStr)

  ############# get string ############# 
  def getStr(self): 
    result = "%s + %s" % (self.space.getStr(), self.time.getStr())
    return result

################################################## 
########### Enodia Space Time base class #########

class EnoSpaceTimeRegistry:
  #warmup example
  events = \
   {'accelerate22':['hbldg:americanhistory.si.edu', ['2022-04-08','2022-04-10']],
    'artisphere22':['clemsonTn:greenvillesc.gov',   ['2022-05-06','2022-05-08']],
   } 
  
  ############# get string ############# 
  def mapEvent2ST(self, event): 
    if event not in self.events: return None
    spaceId, timeId = self.events[event]
    return EnoSpaceTime(spaceId, timeId)

################################
############# main #############

if __name__ == "__main__":
  es1 = EnoSpace("space1")
  es2 = EnoSpace("space2")

  c1 = (es1 ** es2)
  print(c1.getStr())

  estr = EnoSpaceTimeRegistr()
  est3 = estr.mapEvent2ST('accelerate22')
  est4 = estr.mapEvent2ST('artisphere22')
  c2 = (est3 ** est4)
  print(es1.getStr())

### end ###
