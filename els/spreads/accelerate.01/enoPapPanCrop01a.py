#Cropping PDF panels
#Brygg Ullmer, Clemson University
#Begun 2022-03-24

#Draws from code by Sonu Kumar Prashant and bfhaha:
#https://stackoverflow.com/questions/457207/cropping-srcPages-of-a-pdf-file

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
import sys

srcFn = "siMap18a.pdf"

divsHoriz = 6
divsVert  = 3

trimsTBLR = [100, 0, 0, 0]

srcPdf  = PdfFileReader(open(srcFn, "rb"))
srcPage = srcPdf.getPage(0)

targPdf = PdfFileWriter()

ll = srcPage.cropBox.getLowerLeft()
lr = srcPage.cropBox.getLowerRight()
ul = srcPage.cropBox.getUpperLeft()
ur = srcPage.cropBox.getUpperRight()

print(ll, lr, ul, ur)

nul = (int(ul[0]+trimsTBLR[2]), int(ul[1]+trimsTBLR[0]))
nur = (int(ur[0]-trimsTBLR[3]), int(ur[1]+trimsTBLR[0]))

nll = (int(ll[0]+trimsTBLR[2]), int(ll[1]+trimsTBLR[1]))
nlr = (int(lr[0]-trimsTBLR[3]), int(lr[1]+trimsTBLR[1]))

print(nul, nur, nll, nlr)

srcPage.mediaBox.lowerRight = nlr
srcPage.mediaBox.lowerLeft  = nll
srcPage.mediaBox.upperRight = nur
srcPage.mediaBox.upperLeft  = nul

#for example :- my custom coordinates 
#srcPage.mediaBox.lowerRight = (611, 500)
#srcPage.mediaBox.lowerLeft = (0, 500)
#srcPage.mediaBox.upperRight = (611, 700)
#srcPage.mediaBox.upperLeft = (0, 700)

### end ###
