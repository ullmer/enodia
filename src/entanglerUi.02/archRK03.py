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

def getBldgInfo(targetpage):
  page = wptools.page(targetpage, silent=True).get_parse()
  result = ''
  try:
    infobox = page.data['infobox']
    location  = infobox['location'];    result += ('location: %s, ' % location)
    completed = infobox['completed'];   result += ('completed: %s, ' % completed)
    floors    = infobox['Floor count']; result += ('floors: %s, ' % floors)
    roof      = infobox['Roof'];        result += ('roof: %s, ' % roof)
  except: pass
  return result

rkb   = "Category:Rem Koolhaas buildings"
bldgs = getBldgs(rkb)

idx = 0
for b in bldgs:
  idx += 1
  if idx > 7: break

  binfo = getBldgInfo(b)
  print('%s: {%s}' % (b, binfo))

### end ###
