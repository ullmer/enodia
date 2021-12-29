# Wikipedia Parks parsing 
# By Brygg Ullmer, Clemson University
# Begun 2021-12-17; adapting on 2021-12-28

import wikipediaapi
import wptools

##################### get buildings #####################

def getCategoryMembers(targetpage):
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

scParks = "List of South Carolina state parks"
parkEls = getCategoryMembers(rkb)
print(parkEls)

idx = 0
for park in parkEls:
  idx += 1
  if idx > 7: break

  #loc = getBldgLocation(b)
  #print('Building %s : location %s' % (b, loc))

### end ###
