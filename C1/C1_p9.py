from PIL import Image
from pylab import *

# reading image
im = array(Image.open('.\Resource\empire.jpg').convert('L'))



im2 = 255 - im 


im3 = (100.0/255) * im + 100
figure("im3")
gray()
imshow(im3)


im4 = 255.0 * (im/255.0)**2
figure("im4")
gray()
imshow(im4)


show()