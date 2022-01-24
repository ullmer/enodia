#PyGame Zero warmup on timelines
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

from pgzTimeline import *
import traceback, enoDb, sys

pgzt = pgzTimeline("elements.yaml")

TITLE = "Timeline ex02f"
WIDTH = 1920; HEIGHT = 1080

def on_mouse_down(pos):      global pgzt; pgzt.on_mouse_down(pos)
def on_mouse_move(pos, rel): global pgzt; pgzt.on_mouse_move(pos, rel)
def on_mouse_up(pos):        global pgzt; pgzt.on_mouse_up()
def draw():                  global pgzt; screen.clear(); pgzt.draw()

sqliteDbFn   = 'soc.db3'
queriesYFn   = 'soc-queries.yaml'
soc = enoDb(sqliteDbFn, queriesYFn)

divisions = soc.getDivisions()

for division in divisions:
  divFaculty = soc.getFacultyRankExtraLByDivision(division)
  for faculty in divFaculty:
    lastName, rank, extraRole = faculty
    print(division, lastName)
  
### end ###
