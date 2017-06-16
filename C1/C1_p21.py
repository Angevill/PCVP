from PIL import Image
from numpy import array, zeros, sqrt
from scipy.ndimage import filters
from matplotlib import pylab as pl

im = array(Image.open('.\Resource\empire.jpg').convert('L'))
pl.figure("im")
pl.gray()
pl.imshow(im)

SIGMA = 2

imx = zeros(im.shape)
filters.gaussian_filter(im, (SIGMA,SIGMA), (0,1), imx)
pl.figure("imx")
pl.gray()
pl.imshow(imx)

imy = zeros(im.shape)
filters.gaussian_filter(im, (SIGMA,SIGMA), (1,0), imy)
pl.figure("imy")
pl.gray()
pl.imshow(imy)

magnitude = sqrt(imx**2 + imy**2)
pl.figure("magnitude")
pl.imshow(magnitude)

pl.show()