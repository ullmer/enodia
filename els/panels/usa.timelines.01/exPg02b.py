#PyGame Zero warmup on timelines
#Brygg Ullmer, Clemson University
#Begun 2022-01-23

t1, t2 = Actor('1860a'), Actor('1880a')

TITLE = "Timeline ex02a"
WIDTH = 1920; HEIGHT = 1080

t1.topleft= 0,   10
t2.topleft= 600, 10

def on_mouse_down(pos):
  animate(t1, tween='accel_decel', pos=pos, duration=0.5)

  #if t1.collidepoint(pos): updateT1(pos)
  #if t2.collidepoint(pos): updateT2(pos)

def draw():
  screen.clear()
  t1.draw(); t2.draw()

### end ###
