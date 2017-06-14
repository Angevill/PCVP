from PIL import Image
from pylab import *
import rof

im = array(Image.open('.\Resource\empire.jpg').convert('L'))
U,T = rof.denoise(im, im)

figure("ROF_denoise")
gray()
imshow(U)
axis('equal')
axis('off')

show()

