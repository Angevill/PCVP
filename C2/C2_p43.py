import pylab as pl 
import numpy as np 
from PIL import Image 

import sift

imname = '.\Resource\empire.jpg'
im1 = np.array(Image.open(imname).convert('L'))
siftfilename = '.\Resource\empire.sift'
sift.process_image(imname, siftfilename)
l1,d1 = sift.read_features_from_file(siftfilename)

pl.figure()
pl.gray()
sift.plot_features(im1,l1,circle=True)
pl.show()