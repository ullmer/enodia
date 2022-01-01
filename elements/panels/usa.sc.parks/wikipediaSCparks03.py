# Wikipedia Parks parsing 
# By Brygg Ullmer, Clemson University
# Begun 2021-12-17; adapting on 2021-12-28

import wikipediaapi
import wptools
import requests
from bs4 import BeautifulSoup
import sys

##################### get buildings #####################

def getCategoryMembers(targetpage):
  ww=wikipediaapi.Wikipedia('en')
  page1 = ww.page(targetpage)
  categories = page1.categorymembers.keys()
  return categories

def spaceToUnderscore(str):
  result = string.replace(" ", "_")
  return result

def getLinksOrdered(targetpage):  
   links = []

   req = requests.get(targetpage)
   soup = BeautifulSoup(req.content, 'html.parser')
   s2 = soup.find(id="mw-content-text")
   for paragraph in s2:
     try:
       for link in paragraph.find_all("a"): 
         links.append(link["href"])
         #print("FOO>> ", link)
     except: pass
   return links

def getLinks(targetpage):
  ww=wikipediaapi.Wikipedia('en')
  page1 = ww.page(targetpage)
  links = page1.links
  return links

def plausibleTarget(candidateStr):
  targetStrs = ['park', 'site', 'area']
  lowerCandStr = candidateStr.lower()
  for targetStr in targetStrs:
    if lowerCandStr.find(targetStr) != -1: return True
  return False 
  
def withinExclusions(linkKey):
  exclusionStrs = ['List of', 'Template:', 'Template talk:', 'Category:', 'Lists of']
  for exclusionStr in exclusionStrs:
    if linkKey.find(exclusionStr) != -1: return True
  return False

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

#scParks = "List of South Carolina state parks"
#linkHash  = getLinks(scParks)

park1   = "Aiken State Park"
#linkHash  = getLinks(park1)
links = getLinksOrdered("https://en.wikipedia.org/wiki/Aiken_State_Park")

for link in links: print(link)

scParks = "List of South Carolina state parks"
linkHash  = getLinks(scParks)


idx = 0
for linkKey in linkHash.keys():
  idx += 1
  if plausibleTarget(linkKey) and not withinExclusions(linkKey):
    #print(linkKey)
    link2 = spaceToUnderscore(linkKey)
    recordLinks(link2)

### end ###
