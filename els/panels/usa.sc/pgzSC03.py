### end ###

pos1 = (300, 300)
rad1 = 30
col1 = 200, 0, 0
col2 = 250, 100, 100

bg = Actor("sc-map02c")

def draw():
  bg.draw()
  screen.draw.circle(pos1, rad1, col2)
  screen.draw.text("place1", center=pos1, color=col2, alpha=.65)


### end ###
