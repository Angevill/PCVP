import pylab as pl 
import numpy as np
from PIL import Image

import sift
import imtools
import pydot

download_path = "D:\GitHub\PCVP\whitehouse"
path = "D:\GitHub\PCVP\whitehouse"

# list of downloaded filenames
imlist = imtools.get_imlist(download_path)
nbr_images = len(imlist)

# extract features
featlist = [imname[:-3]+'sift' for imname in imlist]

for i,imname in enumerate(imlist):
    sift.process_image(imname, featlist[i])

matchscores = np.zeros((nbr_images, nbr_images))

for i in range(nbr_images):
    for j in range(i, nbr_images): # only compute upper triangle
        print 'comparing {} {}'.format(imlist[i], imlist[j])
        l1,d1 = sift.read_features_from_file(featlist[i])
        l2,d2 = sift.read_features_from_file(featlist[j])
        matches = sift.match_twosided(d1, d2)
        nbr_matches = sum(matches > 0)
        print 'number of matches = {}'.format(nbr_matches) 
        matchscores[i,j] = nbr_matches

# copy values
for i in range(nbr_images):
    for j in range(i+1, nbr_images):
        matchscores[j,i] = matchscores[i,j]

threshold = 2

g = pydot.Dot(graph_type='graph')

for i in range(nbr_images):
    for j in range(i+1, nbr_images):
        if matchscores[i,j] > threshold:
            # first image in pair
            im = Image.open(imlist[i])
            im.thumbnail((100,100))
            filename = path+str(i)+'.png'
            im.save(filename)
            g.add_node(pydot.Node(str(i), fontcolor='transparent', shape='rectangle', image=filename))

            # second image in pair
            im = Image.open(imlist[j])
            im.thumbnail((100,100))
            filename = path+str(j)+'.png'
            im.save(filename) # need temporary files of the right size 
            g.add_node(pydot.Node(str(j),fontcolor='transparent',shape='rectangle',image=filename)) 
            
            g.add_edge(pydot.Edge(str(i),str(j)))

g.write_png('whitehouse_Dot.png')
