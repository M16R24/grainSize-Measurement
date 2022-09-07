# importing necessary libraries

import numpy as np
import matplotlib.pyplot as plt

from skimage import io, color, filters, measure
from scipy import ndimage

from skimage.morphology import erosion, dilation

from IPython.display import display

# ------------------------------------------------------------------------------------------

# custom function to diplay the image

def Image(image):
  print("Image shape: ", image.shape); # prints shape of the image, gray or color image
  
  fig, ax = plt.figure(1, dpi = 100, facecolor = (1, 1, 1));
  ax.imshow(image, cmap = 'gray'); # colormap is set default to gray
  ax.axis('off')
 
# ------------------------------------------------------------------------------------------
  
# import the image

img = io.imread(".images/ferrite.jpeg")
  
