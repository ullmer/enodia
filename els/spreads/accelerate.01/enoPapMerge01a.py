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

########### process YAML spread file ########### 

def procSpreadYaml(spreadYamlFn):
  global spreadHash

  try:    y = yaml.safe_load(spreadYamlFn)
  except: print("procSpreadYaml error on filename", spreadYamlFn); sys.exit(-1)
  
# process list of YAML files

spreadHash = {}

for spreadYamlFn in es:
  procSpreadYaml(spreadYamlFn)

#Below from here: https://gist.github.com/Geekfish/a4fe4efd59e158f55ca5c76479831c8d
def pdf_combine(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    merger.append(pdf)
  merger.write('merge.pdf')

pdf_combine(inputs)

spread:
  - accelerateBC.yaml
  - siMap.yaml

spreadTargFn: "images/spread01.pdf"


### end ###
