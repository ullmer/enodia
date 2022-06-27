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
    compositeStr = "%s entangled with %s" % (
      self.getStr(), other.getStr())

    self.spaceStr = compositeStr

  ############# get string ############# 

  def getStr(self): return self.spaceStr 

################################################## 
############# Enodia Time base class #############

class EnoTime:
  timeStr = None
  beginTime, endTime, currentTime = [None] * 3

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

################################
############# main #############

if __name__ == "__main__":
  es1 = EnoSpace("space1")
  es2 = EnoSpace("space2")

  c1 = (es1 ** es2)
  print(es1.getStr())

### end ###
