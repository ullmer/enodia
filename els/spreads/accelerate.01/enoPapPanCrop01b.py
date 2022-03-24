#Cropping PDF panels
#Brygg Ullmer, Clemson University
#Begun 2022-03-24

#Draws from code by Sonu Kumar Prashant and bfhaha:
#https://stackoverflow.com/questions/457207/cropping-srcPages-of-a-pdf-file

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
import sys

srcFn  = "siMap18a.pdf"
targFn = "siMap18aCr.pdf"

divsHoriz = 6
divsVert  = 3

#trimsTBLR = [200, 200, 200, 200]
#trimsTBLR = [200, 1910, 200, 200] #upper band
trimsTBLR = [300, 1910, 200, 200] #upper band

srcPdf  = PdfFileReader(open(srcFn, "rb"))
srcPage = srcPdf.getPage(0)

targPdf = PdfFileWriter()

ll = srcPage.cropBox.getLowerLeft()
lr = srcPage.cropBox.getLowerRight()
ul = srcPage.cropBox.getUpperLeft()
ur = srcPage.cropBox.getUpperRight()
print(ll, lr, ul, ur)

spreadWidth  = lr[0]-ul[0]
spreadHeight = ur[1]-lr[1]

paneWidth  = int(spreadWidth  / divsHoriz)
paneHeight = int(spreadHeight / divsVert)

cropUL = (int(ul[0]+trimsTBLR[2]), int(ul[1]+trimsTBLR[0]))
cropLR = (int(lr[0]-trimsTBLR[3]), int(lr[1]-trimsTBLR[1]))

#nul = (int(ul[0]+trimsTBLR[2]), int(ul[1]-trimsTBLR[0]))
#nll = (int(ll[0]+trimsTBLR[2]), int(ll[1]+trimsTBLR[1]))
#nur = (int(ur[0]-trimsTBLR[3]), int(ur[1]-trimsTBLR[0]))
#nlr = (int(lr[0]-trimsTBLR[3]), int(lr[1]+trimsTBLR[1]))
#nur = (int(nll[0]+paneWidth), int(ur[1]-trimsTBLR[0]))
#nlr = (int(nll[0]+paneWidth), int(lr[1]+trimsTBLR[1]))
#print(nul, nur, nll, nlr)

srcPage.cropBox.upperLeft  = cropUL
srcPage.cropBox.lowerRight = cropLR

targPdf.addPage(srcPage)
targF = open(targFn, 'wb')

targPdf.write(targF)
targF.close()

### end ###
