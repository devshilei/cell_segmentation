#coding:utf-8
"""
Created on 2018年12月24日

@author: devshilei@gmail.com
"""
from skimage import io, filters

image = io.imread("2.jpg", as_gray=True)
# ... or any other NumPy array!
edges = filters.sobel(image)
io.imshow(edges, cmap="gray")
io.show()