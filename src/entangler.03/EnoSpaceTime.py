# Enodia Space/Time operations
# By Brygg Ullmer and Sida Dai, Clemson University
# Begun 2022-06-26

############# Enodia Space base class #############

class EnoSpace:
  space = None
  def __init__(self, space): self.space = space

  def __pow__(self, other):
    compositeSpace = "%s entangled with %s" % (
      self.space, other.space)

    return EnoSpace(compositeSpace

############# Enodia Time base class #############

class EnoTime:
  space = None
  def __init__(self, time): self.space = time

### end ###
