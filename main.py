# importing necessary libraries

import numpy as np
import matplotlib.pyplot as plt

from skimage import io, color, filters, measure, img_as_float
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
img = img_as_float(img)

# ------------------------------------------------------------------------------------------

# thresholding the image, separate foreground from background

fig, ax = try_all_threshold(img, figsize=(10, 8), verbose=False) # checks threshold with all available methods
plt.show()

img_yen = filters.threshold_yen(img) # of all threshold methods, Yen gives more closest to what we are looking for
Image(img_yen) # displays the image

img = img > img_yen # separating foreground from background

# ------------------------------------------------------------------------------------------

# making the image more clearer, to eliminate the unwanted dark spots
footprint = [[1, 1], [1, 1]]
img_erode = erosion(img, footprint = footprint) # using footprint kernel,the dark spots are further becomes darker
img_dilate = dilation(img_erode) # the eroded image is dilated, something like reducing the pixel strength with respect to adjacent pixels.

Image(img_dilate)

mask = img == 255

structure = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
label_img, num_labels = ndimage.label(mask, structure = structure) # label_img contains all grains detected with respective labeling

img_labeled = color.label2rgb(label_img)
Image(img_labeled) # shows all the grains with color coded.

# Here few grains are clustered with same color, that is due to lack of connectivity with adjacent grain boundaries. Even missing of single pixel count
# in the boundary makes it as a single large grain.

# ------------------------------------------------------------------------------------------

# measuring the grain size

pixels_to_um = 0.5 # here pixel length is converted to micrometer.

props = measure.regionprops(img_labeled, image_intesity_img)
propsList = ['Area', 'quivalent_diameter']

grain_area = []

for i in props:
    grain1_area.append(i.area)
    
fig, ax = plt.subplots(1, 1, dpi = 150, facecolor = (1, 1, 1), edgecolor = '#169acf')
ax.hist(grain_area, bins = 20, alpha = 0.7, label = 'Mean:{}'.format(np.round(np.mean(grain_area)))
ax.axvline(np.mean(grain_area), color = 'red')
ax.legend()
     
     
