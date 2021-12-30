# Wikipedia Parks parsing 
# By Brygg Ullmer, Clemson University
# Begun 2021-12-17; adapting on 2021-12-28

import wikipediaapi
import wptools
import sys
import requests
import urllib3
from bs4 import BeautifulSoup

##################### get buildings #####################

def getCategoryMembers(targetpage):
  ww=wikipediaapi.Wikipedia('en')
  page1 = ww.page(targetpage)
  categories = page1.categorymembers.keys()
  return categories

#next draws from https://stackoverflow.com/questions/18916616/get-first-link-of-wikipedia-article-using-wikipedia-api

def isValid(ref,paragraph): #by Christopher Chiche, per above
   if not ref or "#" in ref or "//" in ref or ":" in ref: return False
   if "/wiki/" not in ref:   return False
   if ref not in paragraph:  return False
   prefix = paragraph.split(ref,1)[0]
   if prefix.count("(")!=prefix.count(")"): return False
   return True

def validateTag(tag): #by Christopher Chiche, per above
   name = tag.name
   isParagraph = name == "p"
   isList = name == "ul"
   return isParagraph or isList

def getLinksOrdered(targetpage):  
   links = []

   req = requests.get(targetpage)
   soup = BeautifulSoup(req.content, 'html.parser')
   soup = soup.find(id="mw-content-text")
   for paragraph in soup.find_all(validateTag, recursive=False):
      for link in paragraph.find_all("a"):
         links.append(link)
         #ref = link.get("href")
         #if isValid(str(ref),str(paragraph)):
         #   links.append(link)
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
print(links)

#idx = 0
#for linkKey in linkHash.keys():
#  idx += 1
#  if plausibleTarget(linkKey) and not withinExclusions(linkKey):
#    print(linkKey)


### end ###
