### end ###

pos1 = (300, 300)
rad1 = 100
col1 = 200, 0, 0

bg = Actor("sc-map02b")

def draw():
  bg.draw()
  screen.draw.filled_circle(pos1, rad1, col1)
  screen.draw.text("place1", pos1, color="orange")

#screen.draw.circle(pos1, rad1, col1)
#screen.draw.circle(pos1, rad1, col1, width=4)

### end ###
