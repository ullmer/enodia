# Wikipedia Parks parsing 
# By Brygg Ullmer, Clemson University
# Begun 2021-12-17; adapting on 2021-12-28

import wikipediaapi
import wptools


#parks, site, area

##################### get buildings #####################

def getCategoryMembers(targetpage):
  ww=wikipediaapi.Wikipedia('en')
  page1 = ww.page(targetpage)
  categories = page1.categorymembers.keys()
  return categories

def getLinks(targetpage):
  ww=wikipediaapi.Wikipedia('en')
  page1 = ww.page(targetpage)
  links = page1.links()
  return links

################## get building location ##################

#def getBldgLocation(targetpage):
#  page = wptools.page(targetpage, silent=True).get_parse()

################## get building location ##################

def getBldgLocation(targetpage):
  page = wptools.page(targetpage, silent=True).get_parse()
  try:
    infobox = page.data['infobox']
    location = infobox['location']
    return location
  except: return None

scParks = "List of South Carolina state parks"
#parkEls = getCategoryMembers(scParks)
linkHash  = getLinks(scParks)

idx = 0
for link in linkHash.keys():
  idx += 1
  if idx > 7: break
  print(linkHash[link])

  #loc = getBldgLocation(b)
  #print('Building %s : location %s' % (b, loc))

### end ###
