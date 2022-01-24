#PyGame Zero warmup on timelines
#Brygg Ullmer, Clemson University
#Begun 2022-01-23

t1, t2 = Actor('1860a'), Actor('1880a')

TITLE = "Timeline ex02a"
WIDTH = 1920; HEIGHT = 1080

t1.topleft= 0,   10
t2.topleft= 600, 10

def draw():
  screen.clear()
  t1.draw(); t2.draw()

### end ###
