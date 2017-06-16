
from pylab import *
from numpy import *
from PIL import Image

import sift
import harris

"""
This is the twosided SIFT feature matching example from Section 2.2 (p 44).
"""

imname1 = '.\Resource\climbing_1_small.jpg'
imname2 = '.\Resource\climbing_2_small.jpg'

# process and save features to file
siftim1 = '.\Resource\climbing_1_small.sift'
siftim2 = '.\Resource\climbing_2_small.sift'
sift.process_image(imname1, siftim1)
sift.process_image(imname2, siftim2)

# read features and match
l1,d1 = sift.read_features_from_file(siftim1)
l2,d2 = sift.read_features_from_file(siftim2)
matchscores = sift.match_twosided(d1, d2)

# load images and plot
im1 = array(Image.open(imname1))
im2 = array(Image.open(imname2))

sift.plot_matches(im1,im2,l1,l2,matchscores,show_below=True)
show()