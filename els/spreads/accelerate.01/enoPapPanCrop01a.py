#Cropping PDF panels
#Brygg Ullmer, Clemson University
#Begun 2022-03-24

#Draws heavily from code by Sonu Kumar Prashant:
#https://stackoverflow.com/questions/457207/cropping-pages-of-a-pdf-file

#present code below is verbatim; about to evolve

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
import sys

srcFn = "siMap18a.pdf"

divsHoriz = 6
divsVert  = 3

trimsTBLR = [100, 0, 0, 0]

pdf_file = PdfFileReader(open(srcFn, "rb"))
page = pdf_file.getPage(0)

ll = page.cropBox.getLowerLeft()
lr = page.cropBox.getLowerRight()
ul = page.cropBox.getUpperLeft()
ur = page.cropBox.getUpperRight()

print(ll, lr, ul, ur)

#  (lower_right_new_x_coordinate, lower_right_new_y_coordinate)

#https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel

#newCoords  = {}
#origCoords = [ll, lr, ul, ur]; newCoordIdxs = ["ll", "lr", "ul", "ur"]
#for origCoord, newCoordIdx in zip(origCoords, newCoordIdxs):
#  newCoords[newCoordIdx] = origCoord

nul = (int(ul[0]+trimsTBLR[2]), int(ul[1]+trimsTBLR[0]))
nur = (int(ur[0]-trimsTBLR[3]), int(ur[1]+trimsTBLR[0]))

nll = (int(ll[0]+trimsTBLR[2]), int(ll[1]+trimsTBLR[1]))
nlr = (int(lr[0]-trimsTBLR[3]), int(lr[1]+trimsTBLR[1]))

#ul2 = newCoords["ul"]
#newCoords["ul"][1] += trimsTBLR[0]; 

print(nul, nur, nll, nlr)

page.mediaBox.lowerRight = nlr
page.mediaBox.lowerLeft  = nll
page.mediaBox.upperRight = nur
page.mediaBox.upperLeft  = nul

#for example :- my custom coordinates 
#page.mediaBox.lowerRight = (611, 500)
#page.mediaBox.lowerLeft = (0, 500)
#page.mediaBox.upperRight = (611, 700)
#page.mediaBox.upperLeft = (0, 700)

### end ###
