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

trimsTBLR = [0, 0, 0, 0]

pdf_file = PdfFileReader(open(srcFn, "rb"))
page = pdf_file.getPage(0)

ll = page.cropBox.getLowerLeft()
lr = page.cropBox.getLowerRight()
ul = page.cropBox.getUpperLeft()
ur = page.cropBox.getUpperRight()

print(ll, lr, ul, ur)

#  (lower_right_new_x_coordinate, lower_right_new_y_coordinate)

#https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel

newCoords  = {}
origCoords = [ll, lr, ul, ur]; newCoordIdxs = ["ll", "lr", "ul", "ur"]
for origCoord, newCoordIdx in zip(origCoords, newCoordIdxs):
  newCoords[newCoordIdx] = origCoord

print(newCoords)
sys.exit(-1)

ll_nx_coord = ll[0]; ll_ny_coord = ll[1]
ll_

page.mediaBox.lowerRight = (lr_nx_coord, lr_ny_coord)
page.mediaBox.lowerLeft  = (ll_nx_coord, ll_ny_coord)
page.mediaBox.upperRight = (ur_nx_coord, ur_ny_coord)
page.mediaBox.upperLeft  = (ul_nx_coord, ul_ny_coord)

#for example :- my custom coordinates 
#page.mediaBox.lowerRight = (611, 500)
#page.mediaBox.lowerLeft = (0, 500)
#page.mediaBox.upperRight = (611, 700)
#page.mediaBox.upperLeft = (0, 700)

### end ###
