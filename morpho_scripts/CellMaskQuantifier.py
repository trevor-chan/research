#!/usr/bin/env python3

import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

from numpy import asarray
from PIL import Image
from skimage.draw import ellipse
from skimage.measure import label, regionprops, regionprops_table
from skimage.transform import rotate

### Uses numpy, skimage, pillow


images = []
regions = []

#Load images, convert to np array
for image_path in glob.glob(sys.argv[1] + '/*.png'): #filepath of folder
    #print(image_path)
    img = Image.open(image_path)
    images.append(asarray(img))

for img in images:
    img = label(img) #labels connected regions
    regions.append(regionprops(img))
    #regions[index] list with properties accesible: see
    #https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops




#Plot
fig, ax = plt.subplots()
ax.axis((0, 256, 256, 0))
img_combined = np.sum([np.expand_dims(img, 0) for img in images], axis=0)
img_combined = np.transpose(img_combined, (1, 2, 0))
ax.imshow(img_combined[:,:,0], cmap=plt.cm.gray)


for index, img in enumerate(images):

    for props in regions[index]:
        y0, x0 = props.centroid
        orientation = props.orientation
        x1 = x0 + math.cos(orientation) * 0.5 * props.minor_axis_length
        y1 = y0 - math.sin(orientation) * 0.5 * props.minor_axis_length
        x2 = x0 - math.sin(orientation) * 0.5 * props.major_axis_length
        y2 = y0 - math.cos(orientation) * 0.5 * props.major_axis_length

        ax.plot((x0, x1), (y0, y1), '-r', linewidth=1)
        ax.plot((x0, x2), (y0, y2), '-r', linewidth=1)
        ax.plot(x0, y0, '.g', markersize=15)

        minr, minc, maxr, maxc = props.bbox
        bx = (minc, maxc, maxc, minc, minc)
        by = (minr, minr, maxr, maxr, minr)
        ax.plot(bx, by, '-b', linewidth=1)



plt.show()
