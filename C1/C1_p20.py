from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('.\Resource\empire.jpg').convert('L'))

imx = zeros(im.shape)
filters.sobel(im, 1, imx)
figure("imx")
gray()
imshow(imx)

imy = zeros(im.shape)
filters.sobel(im, 0, imy)
figure("imy")
gray()
imshow(imy)

magnitude = sqrt(imx**2 + imy**2)
figure("magnitude")
gray()
imshow(magnitude)

show()