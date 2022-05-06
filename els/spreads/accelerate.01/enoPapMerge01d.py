#Merging PDF panels
#Brygg Ullmer, Clemson University
#Begun 2022-03-26
#Reworked 2022-05-05

#Draws from code by geekfish:
#https://gist.github.com/Geekfish/a4fe4efd59e158f55ca5c76479831c8d

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
from PyPDF2.pdf import PageObject

import yaml, sys, os, glob

from enoSpreadDividers import *

fnPrefix = "images/"

if len(sys.argv) != 2:
  print("Please provide .yaml filename as argument"); sys.exit(-1)

srcYamlFn = sys.argv[1] #e.g., 'spreadSeq01.yaml'

srcYamlF  = open(srcYamlFn, "rt")
srcYaml   = yaml.safe_load(srcYamlF)

try:    es = srcYaml["spread"]
except: print("YAML spread error; aborting"); sys.exit(-1)

try:    spreadTargDir = srcYaml["spreadTargDir"]
except: print("YAML error: no spreadTargFn; aborting"); sys.exit(-1)

try:    print("attempting to create directory", spreadTargDir); os.mkdir(spreadTargDir)
except: pass

########### process YAML spread file ########### 

def procSpreadYaml(spreadYamlFn):
  global fnPrefix, spreadHash

  yf = open(spreadYamlFn, "rt")
  try:    y = yaml.safe_load(yf)
  except: print("procSpreadYaml error on filename", spreadYamlFn); sys.exit(-1)

  if "enoSpread" in y: spread  = y["enoSpread"]
  else:                
    print("procSpreadYaml error: no enoSpread in filename", spreadYamlFn); print(y); sys.exit(-1)

  if "targDir" in spread: targDir = spread["targDir"]
  else:                  
    print("procSpreadYaml error: no targDir enoSpread in file enoSpread:", spreadYamlFn); sys.exit(-1)

  targpat = fnPrefix + targDir + "/*.pdf"
  files = glob.glob(targpat)
  spreadHash[targDir] = files
  return targDir
  
# process list of YAML files

spreadHash = {}

for spreadYamlFn in es:
  procSpreadYaml(spreadYamlFn)

########### pdf combine ########### 

def pdfCombine(srcPdfs, targPdf):
  print("pdfCombine src:", srcPdfs, "; targPdf:", targPdf)

  pages    = []
  srcFList = []

  for pdfFn in srcPdfs:
    f = open(pdfFn, 'rb')
    reader = PdfFileReader(f)
    pages.append(reader.getPage(0))
    srcFList.append(f)

  widthSum = 0; maxHeight = 0
  for page in pages: 
    widthSum += page.mediaBox.getWidth() 
    h         = page.mediaBox.getHeight()
    if h > maxHeight: maxHeight = h

  mergedPage = PageObject.createBlankPage(None, widthSum, maxHeight)
  firstPage = True; dx=0

  for page in pages:
    mergedPage.mergeTranslatedPage(page, dx, 0)
    dx += page.mediaBox.getWidth()

  writer = PdfFileWriter()
  writer.addPage(mergedPage)

  f = open(targPdf, "wb")
  writer.write(f)
  f.close()

  for f in srcFList: f.close() # seeks present both in bbox query & merge

########### main ########### 

spreadHashKeys = spreadHash.keys()
firstKey = list(spreadHashKeys)[0]
print("first key:", firstKey)

panelPdfs = spreadHash[firstKey]
#print(spreadHash)

esd = enoSpreadDividers()

for panelPdfFnRaw in panelPdfs:
  panelPdfFn = os.path.basename(panelPdfFnRaw)
  
  srcPdfs = []
  for srcPdf in spreadHashKeys: srcPdfs.append(fnPrefix + srcPdf + "/" + panelPdfFn)

  pdfbn = os.path.basename(panelPdfFn)
  targPdf = spreadTargDir + pdfbn
  pdfCombine(srcPdfs, targPdf)

### end ###
