from PIL import Image
from numpy import array, zeros, sqrt
from scipy.ndimage import filters
from matplotlib import pylab

im = array(Image.open('.\Resource\empire.jpg').convert('L'))
pylab.figure("im")
pylab.gray()
pylab.imshow(im)

SIGMA = 2

imx = zeros(im.shape)
filters.gaussian_filter(im, (SIGMA,SIGMA), (0,1), imx)
pylab.figure("imx")
pylab.gray()
pylab.imshow(imx)

imy = zeros(im.shape)
filters.gaussian_filter(im, (SIGMA,SIGMA), (1,0), imy)
pylab.figure("imy")
pylab.gray()
pylab.imshow(imy)

magnitude = sqrt(imx**2 + imy**2)
pylab.figure("magnitude")
pylab.imshow(magnitude)

pylab.show()