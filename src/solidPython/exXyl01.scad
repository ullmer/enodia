// Generated by SolidPython 1.1.1 on 2021-10-28 00:38:58
$fn = 25;


union() {
	translate(v = [0, 0, 0]) {
		cube(size = [1.1875000000, 10.2500000000, 0.6250000000]);
	}
	translate(v = [1.4375000000, 0, 0]) {
		cube(size = [1.1875000000, 9.8750000000, 0.6250000000]);
	}
	translate(v = [2.8750000000, 0, 0]) {
		cube(size = [1.1875000000, 9.7500000000, 0.6250000000]);
	}
	translate(v = [4.3125000000, 0, 0]) {
		cube(size = [1.1875000000, 9.3125000000, 0.6250000000]);
	}
	translate(v = [5.7500000000, 0, 0]) {
		cube(size = [1.1875000000, 9, 0.6250000000]);
	}
	translate(v = [7.1875000000, 0, 0]) {
		cube(size = [1.1875000000, 8.6250000000, 0.6250000000]);
	}
	translate(v = [8.6250000000, 0, 0]) {
		cube(size = [1.1875000000, 8.3125000000, 0.6250000000]);
	}
	translate(v = [10.0625000000, 0, 0]) {
		cube(size = [1.1875000000, 8.0625000000, 0.6250000000]);
	}
	translate(v = [11.5000000000, 0, 0]) {
		cube(size = [1.1875000000, 7.7500000000, 0.6250000000]);
	}
	translate(v = [12.9375000000, 0, 0]) {
		cube(size = [1.1875000000, 7.4375000000, 0.6250000000]);
	}
	translate(v = [14.3750000000, 0, 0]) {
		cube(size = [1.1875000000, 7.0625000000, 0.6250000000]);
	}
	translate(v = [15.8125000000, 0, 0]) {
		cube(size = [1.1875000000, 6.8125000000, 0.6250000000]);
	}
	translate(v = [17.2500000000, 0, 0]) {
		cube(size = [1.1875000000, 6.4375000000, 0.6250000000]);
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-28

from       solid import * # load in SolidPython/SCAD support code
from synthShapes import *
import yaml

yfn = 'xylophone.yaml'
yf  = open(yfn, 'r')
yd  = yaml.safe_load(yf)

barWidth   = convertFractional(yd['allBars']['wide'])
barThick   = convertFractional(yd['allBars']['thick'])
between    = convertFractional(yd['allBars']['between'])
barLengths = convertFractionalList(yd['lengths'])

#print(barWidth, barThick, barLengths)

outGeom = None; offset = 0
for barLength in barLengths:
  c1 = cube([barWidth, barLength, barThick])
  c2 = translate([offset,0,0])(c1)

  if outGeom == None: outGeom = c2
  else:               outGeom += c2
  offset += barWidth + between

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exXyl01.scad', file_header=hdr) # write the .scad file

### end ###

 
 
************************************************/
