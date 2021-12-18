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
    infobox  = page.data['infobox']
    location = infobox['location'];      result += ('location: "%s", ' % location)
    opening  = infobox['opening'];       result += ('opening: "%s", ' % opening)
    floors   = infobox['floor_count'];   result += ('floors: "%s", ' % floors)
    roof     = infobox['roof'];          result += ('roof: "%s", ' % roof)
    type     = infobox['building_type']; result += ('bldgType: "%s", ' % type)
  except: pass
  return result

rkb  = "Category:Rem Koolhaas buildings"
scs  = "Category:Santiago_Calatrava_structures"
mvdr = "Category:Ludwig_Mies_van_der_Rohe_buildings"
#bldgs = getBldgs(rkb)
#bldgs = getBldgs(scs)
bldgs = getBldgs(mvdr)

idx = 0
for b in bldgs:
  idx += 1
  #if idx > 7: break

  binfo = getBldgInfo(b)
  print('%s: {%s}' % (b, binfo))

### end ###
