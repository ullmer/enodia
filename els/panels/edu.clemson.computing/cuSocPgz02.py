#Clemson University School of Computing faculty interaction
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

from enoElements import *
from enoDb       import *
import traceback, sys
#import pgzrun

TITLE = "Clemson Computing people"
#WIDTH = 1920; HEIGHT = 1080
WIDTH = 1400; HEIGHT = 850

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
    names.append(lastName)

people = enoElements(names)

numNames  = len(names); halfNames = int(numNames / 2)
firstHalf = names[0:halfNames]; secondHalf = names[halfNames:]
clusterDict = {}
clusterDict['first'] = firstHalf; clusterDict['last'] = secondHalf

cluster1 = enoElClusters(clusterDict)
cluster1.printSummary()
people.animToClusters(cluster1)

def on_mouse_down(pos):      global people; people.on_mouse_down(pos)
def on_mouse_move(pos, rel): global people; people.on_mouse_move(pos, rel)
def on_mouse_up(pos):        global people; people.on_mouse_up()
def draw():                  global people; screen.clear(); people.draw()

### end ###
