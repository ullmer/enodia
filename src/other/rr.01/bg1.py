# L & B, 2022-05-18

import yaml

f   = open("bg1.yaml", "r")
bg1 = yaml.safe_load(f)

cells = bg1["cells"]
colors = cells.keys()

tracking = {}

for color in colors:
  vals    = cells[color]
  numvals = len(vals)
  print(color, numvals)
  for val in vals:
     tracking[val] = color

for i in range(150):
  if i not in tracking: print(i)

### end ###
