#coding:utf-8
"""
Created on 2018年12月20日

@author: devshilei@gmail.com
"""
# from skimage import io, filters
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import collections

img = Image.open("1.jpg")
gray = img.convert("L")
print(np.min(gray), np.max(gray))
im_array = np.array(img)
flatten_array = im_array.flatten()
print(flatten_array.shape)
pix_set = set(flatten_array.tolist())
c = collections.Counter(flatten_array)
for k, v in c.items():
    print(k, v)
print(c)
print(len(pix_set))
print(pix_set)
plt.axis('off') # 不显示坐标轴
plt.imshow(gray, cmap="gray")
plt.show()