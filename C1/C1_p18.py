from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('.\Resource\empire.jpg').convert('L'))

im2 = filters.gaussian_filter(im, 5)
figure("im2")
gray()
imshow(im2)

show()