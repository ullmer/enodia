#Cropping PDF panels
#Brygg Ullmer, Clemson University
#Begun 2022-03-24

#Draws from code by winosli:
#https://gist.github.com/Geekfish/a4fe4efd59e158f55ca5c76479831c8d

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
import yaml
import sys, os, glob

fnPrefix = "images/"

if len(sys.argv) != 2:
  print("Please provide .yaml filename as argument"); sys.exit(-1)

srcYamlFn = sys.argv[1]

srcYamlF  = open(srcYamlFn, "rt")
srcYaml   = yaml.safe_load(srcYamlF)

try:    es = srcYaml["spread"]
except: print("YAML spread error; aborting"); sys.exit(-1)

try:    spreadTargDir = fnPrefix + srcYaml["spreadTargDir"]
except: print("YAML error: no spreadTargFn; aborting"); sys.exit(-1)

try:    os.mkdir(spreadTargDir)
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

  targpat = fnPrefix + targDir + "/*"
  files = glob.glob(targpat)
  spreadHash[targDir] = files
  return targDir
  
# process list of YAML files

spreadHash = {}

for spreadYamlFn in es:
  procSpreadYaml(spreadYamlFn)

########### pdf combine ########### 

def pdfCombine(srcPdfs, targPdf):
  global spreadTargFn

  merger = PyPDF2.PdfFileMerger()
  for pdf in srcPdfs:
    merger.append(pdf)
  merger.write(targPdf)

########### main ########### 

keys = spreadHash.keys()
firstKey = list(keys)[0]
print("first key:", firstKey)

firstKeyPdfs = spreadHash[firstKey]

for pdf in firstKeyPdfs:
  srcPdfs = []
  for key in keys: srcPdfs.append(key + "/" + pdf)
  targPdf = spreadTargDir + pdf

print(spreadHash)
#pdf_combine(inputs)

### end ###
