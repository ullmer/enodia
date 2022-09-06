# Enodia Fargate planner
# Brygg Ullmer, Clemson University
# Begun 2022-09-05

WIDTH  = 1920
HEIGHT = 1024

fn1 = "mri-fargate-08b1b"
fn2 = "mri-fargate-08b2b"

apos = (150, 150)

a1 = Actor(fn1, pos=apos)
a2 = Actor(fn2, pos=apos)
actors = [a2, a1]

################# draw #################

def draw(): 
  screen.clear()
  for actor in actors: 
    actor.draw()

### end ###
