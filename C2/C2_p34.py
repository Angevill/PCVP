from PIL import Image
import pylab as pl 
import numpy as np 

import harris

im = np.array(Image.open('.\Resource\empire.jpg').convert('L'))

harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim, 6, threshold=0.01)

#harris.plot_harris_points(im, filtered_coords)

# plot only 200 strongest
harris.plot_harris_points(im, filtered_coords[:1200], "NewOne")