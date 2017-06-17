import numpy as np 
import pylab as pl 
from PIL import Image

import warp

# example of affine warp of im1 onto im2
im1 = np.array(Image.open('.\Resource\beatles.jpg').convert('L'))
im2 = np.array(Image.open('.\Resource\sf_view1.jpg').convert('L'))

# set to points
tp = np.array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])

im3 = warp.image_in_image(im1, im2, tp)

pl.figure()
pl.gray()
pl.imshow(im3)
pl.axis('equal')
pl.axis('off')
pl.show()
