# Lilleken & Brygg
# Begun 2022-05-16

WIDTH  = 800
HEIGHT = 800

rr = Actor('redrocket1')
rr.pos = 100, 700

def draw(): #main drawing loop
  screen.clear()
  rr.draw()

def on_key_down(key, mod, unicode):
  x, y = rr.center
  
  if key == keys.LEFT:  animate(rr, center=(x-50, y))
  if key == keys.RIGHT: animate(rr, center=(x+50, y))
  if key == keys.SPACE: animate(rr, center=(x, y-1000))

### end ###
