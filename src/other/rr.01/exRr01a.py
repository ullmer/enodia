# Brygg Ullmer & Lilleken
# Begun 2022-05-16

WIDTH  = 800
HEIGHT = 800

rr = Actor('redrocket1')
rr.pos = 100, 100

def draw(): #main drawing loop
  rr.draw()

def on_key_down(key, mod, unicode):  
  if key == keys.LEFT:  rr.left -= 5 #left  pushed
  if key == keys.RIGHT: rr.left += 5 #right pushed
  if key == keys.SPACE: pass

### end ###
