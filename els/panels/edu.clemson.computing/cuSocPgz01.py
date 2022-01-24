#PyGame Zero warmup on timelines
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

from pgzPeople import *
from enoDb     import *
import traceback, sys

TITLE = "Clemson Computing people"
#WIDTH = 1920; HEIGHT = 1080
WIDTH = 1200; HEIGHT = 800

sqliteDbFn   = 'soc.db3'
queriesYFn   = 'soc-queries.yaml'
soc = enoDb(sqliteDbFn, queriesYFn)

divisions = soc.getDivisions([])
names     = []

for division in divisions:
  divFaculty = soc.getFacultyRankExtraLByDivision(division)
  #print(division, divFaculty)

  for faculty in divFaculty:
    lastName, rank, extraRole = faculty
    #print(division, lastName)
    names.append(lastName)

#snames = names.sort()
snames = names
print(snames)

pgzp = pgzPeople(snames)

def on_mouse_down(pos):      global pgzp; pgzp.on_mouse_down(pos)
def on_mouse_move(pos, rel): global pgzp; pgzp.on_mouse_move(pos, rel)
def on_mouse_up(pos):        global pgzp; pgzp.on_mouse_up()
def draw():                  global pgzp; screen.clear(); pgzp.draw()
  
### end ###
