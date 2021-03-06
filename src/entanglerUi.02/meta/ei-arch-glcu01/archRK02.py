# Wikipedia Architecture parsing 
# By Brygg Ullmer, Clemson University
# Begun 2021-12-17

import wikipediaapi
import wptools

##################### get buildings #####################

def getBldgs(targetpage):
  ww=wikipediaapi.Wikipedia('en')
  page1 = ww.page(targetpage)
  buildings = page1.categorymembers.keys()
  return buildings

################## get building location ##################

def getBldgLocation(targetpage):
  page = wptools.page(targetpage, silent=True).get_parse()
  try:
    infobox = page.data['infobox']
    location = infobox['location']
    return location
  except: return None

rkb   = "Category:Rem Koolhaas buildings"
bldgs = getBldgs(rkb)

idx = 0
for b in bldgs:
  idx += 1
  if idx > 7: break

  loc = getBldgLocation(b)
  print('Building %s : location %s' % (b, loc))

### end ###
