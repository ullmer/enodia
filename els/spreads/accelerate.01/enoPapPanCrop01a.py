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
print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())

sys.exit(-1)

page.mediaBox.lowerRight = (lower_right_new_x_coordinate, lower_right_new_y_coordinate)
page.mediaBox.lowerLeft = (lower_left_new_x_coordinate, lower_left_new_y_coordinate)
page.mediaBox.upperRight = (upper_right_new_x_coordinate, upper_right_new_y_coordinate)
page.mediaBox.upperLeft = (upper_left_new_x_coordinate, upper_left_new_y_coordinate)

#for example :- my custom coordinates 
#page.mediaBox.lowerRight = (611, 500)
#page.mediaBox.lowerLeft = (0, 500)
#page.mediaBox.upperRight = (611, 700)
#page.mediaBox.upperLeft = (0, 700)

### end ###
