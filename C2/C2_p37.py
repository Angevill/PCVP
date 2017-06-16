from PIL import Image
import pylab as pl 
import numpy as np 
import harris
from imtools import imresize
import datetime

WID = 5

im1 = np.array(Image.open('.\Resource\crans_1_small.jpg').convert('L'))
im2 = np.array(Image.open('.\Resource\crans_2_small.jpg').convert('L'))

im1 = imresize(im1, (im1.shape[1]/2,im1.shape[0]/2))
im2 = imresize(im2, (im2.shape[1]/2,im2.shape[0]/2))


harrisim1 = harris.compute_harris_response(im1, 5)
filtered_coords1 = harris.get_harris_points(harrisim1, WID+1)
d1 = harris.get_descriptors(im1, filtered_coords1, WID)

harrisim2 = harris.compute_harris_response(im2, 5)
filtered_coords2 = harris.get_harris_points(harrisim2, WID+1)
d2 = harris.get_descriptors(im2, filtered_coords2, WID)

print "start matching:{}".format(datetime.datetime.now())

matches = harris.match_twosided(d1,d2)

pl.figure()
pl.gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches[:100])

print "finish matching:{}".format(datetime.datetime.now())
pl.show()