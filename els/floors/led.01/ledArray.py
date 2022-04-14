# Library support for 2D LED strip arrays
# By Brygg Ullmer and Sida Dai, Clemson University
# Begun 2022-04-13

try: #https://github.com/v923z/micropython-ulab
    from ulab import numpy
    from ulab import scipy

except ImportError:
    import numpy
    import scipy.special

x = numpy.array([1, 2, 3])

### end ###
