from PIL import Image
import os
import numpy as np 
import pylab as pl 


def process_image(imagename, resultname, params="--edge-thresh 10 --peak-thresh 5"):
    """ Process an image and save the results in a file """

    if imagename[-3:0] != 'pgm':
        # create a pgm file
        im = Image.open(imagename).convert('L')
        imagename = 'tmp.pgm'
        im.save(imagename)

    #cmmd = str("sift" + imagename + " --output=" + resultname + " " + params)
    cmmd = "sift {} --output={} {}".format(imagename,resultname,params)
    

    os.system(cmmd)
    print 'processed {} to {}'.format(imagename, resultname)

def read_features_from_file(filename):
    """ Read feature properties and return in matrix form."""

    f = np.loadtxt(filename)
    return f[:,:4], f[:,4:] # feature locations, descriptors

def write_feathres_to_file(filename, locs, desc):
    """ Save feature location and descriptor to file."""

    np.savetxt(filename, np.hstack((locs, desc)))

def plot_features(im, locs, circle=False):
    """
    Show image with features.

    input: im (image as array), locs (row, col, scale, orientation of each feature). 
    """

    def draw_circle(c, r):
        t = np.arange(0,1.01,.01)*2*np.pi 
        x = r*np.cos(t) + c[0]
        y = r*np.sin(t) + c[1]
        pl.plot(x,y,'b',linewidth=1)

    pl.imshow(im)
    if circle:
        for p in locs:
            draw_circle(p[:2],p[2])
    else:
        pl.plot(locs[:,0],locs[:,1],'ob')
    pl.axis('off')

def match(desc1, desc2):
    """
    For each descriptor in the first image,
    select its match in the second image.
    
    input: desc1 (descriptors for the first image),
    desc2 (same for second image).
    """

    desc1 = np.array([d/np.linalg.norm(d) for d in desc1])
    desc2 = np.array([d/np.linalg.norm(d) for d in desc2])

    dist_ratio = 0.6
    desc1_size = desc1.shape

    matchscores = np.zeros((desc1_size[0]), 'int')
    desc2t = desc2.T # precompute matrix transpose

    for i in range(desc1_size[0]):
        dotprods = np.dot(desc1[i,:], desc2t) # vector of dot products
        dotprods = 0.9999*dotprods
        # inverse cosine and sort, return index for features in second image
        index = np.argsort(np.arccos(dotprods))

        # check if nearest neighbor has angle less than dist_ratio times 2nd
        if np.arccos(dotprods)[index[0]] < dist_ratio * np.arccos(dotprods)[index[1]]:
            matchscores[i]  = int(index[0])

    return matchscores

def match_twosided(desc1, desc2):
    """
    Two-sided symmetric version of match().
    """

    matches_12 = match(desc1, desc2)
    matches_21 = match(desc2, desc1)

    ndx_12 = matches_12.nonzero()[0]

    # remove matches that are not symmetric
    for n in ndx_12:
        if matches_21[int(matches_12[n])] != n:
            matches_12[n] = 0

    return matches_12