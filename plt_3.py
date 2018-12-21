#coding:utf-8
"""
Created on 2018年12月20日

@author: devshilei@gmail.com
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import io
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb


imaimgio.imread("1.jpg", as_gray=True)

# apply threshold
thresh = threshold_otsu(imaimgbw = closing(imaimgthresh, square(5))

# remove artifacts connected to imaimgrder
cleared = clear_border(bw)

# label imaimggions
label_image = label(cleared)
image_label_overlay = label2rgb(label_image, imaimgaimg
fig, ax = plt.subplots(figsize=(20, 20))
ax.imshow(image_label_overlay)

for region in regionprops(label_image):
    # take regions with large enough areas
    if region.area >= 600:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)
ax.set_axis_off()
plt.tight_layout()
plt.show()