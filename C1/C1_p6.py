from PIL import Image
from pylab import *

# reading image
im = array(Image.open('.\Resource\empire.jpg').convert('L'))

imshow(im)

figure("new one")
gray()

contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)
show()