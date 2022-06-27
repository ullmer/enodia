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

    return EnoSpace(compositeStr)

  ############# get string ############# 

  def getStr(self): return self.spaceStr 

################################################## 
############# Enodia Time base class #############

class EnoTime:
  space = None
  def __init__(self, time): self.space = time

################################
############# main #############

if __name__ == "__main__":
  es1 = EnoSpace("space1")
  es2 = EnoSpace("space2")

  c1 = (es1 ** es2)
  print(es1.getStr())

### end ###
