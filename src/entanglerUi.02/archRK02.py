# Wikipedia Architecture parsing 
# By Brygg Ullmer, Clemson University
# Begun 2021-12-17

import wikipediaapi
import wptools

%%%%%%%%%%%%%%%%% get buildings %%%%%%%%%%%%%%%%%

def getBldgs(targetpage):
  ww=wikipediaapi.Wikipedia('en')
  page1 = ww.page(targetpage)
  buildings = page1.categorymembers.keys()
  return buildings

%%%%%%%%%%%%%%%%% get building location %%%%%%%%%%%%%%%%%

def getBldgLocation(targetpage):
  page = wptools.page(targetpage).get_parse()
  infobox = page2.data['infobox']
  location = infobox['location']
  return location

rkb   = "Category:Rem Koolhaas buildings"
bldgs = getBldgs(rkb)

for i in range(3):
  b = bldgs[i]
  loc = getBldgLocation(b)
  print('Building %s : location %s' % (b, loc))

### end ###
