from scipy import ndimage
from PIL import Image
import pylab as pl 
import numpy as np 

im = np.array(Image.open('.\Resource\empire.jpg').convert('L'))
H = np.array([[1.4,0.05,-100], [0.05,1.5,-100], [0,0,1]])
im2 = ndimage.affine_transform(im, H[:2,:2], (H[0,2],H[1,2]))

pl.figure()
pl.gray()
pl.imshow(im2)
pl.show()