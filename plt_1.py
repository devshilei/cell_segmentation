#coding:utf-8
"""
Created on 2018年12月20日

@author: devshilei@gmail.com
"""
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,color,data,filters
camera_man = data.camera()
print(camera_man.shape)

camera_man.rgb2gray(plt.imread("1.jpg"))
print(camera_man)
denoised = filters.rank.median(camera_man.disk(2)) #过滤噪声

#将梯度值低于10的作为开始标记点
markers = filters.rank.gradient(denoised, morphology.disk(5)) <10
markers = ndi.label(markers)[0]

gradient = filters.rank.gradient(denoised, morphology.disk(2)) #计算梯度
labels =morphology.watershed(gradient, markers, mask=camera_man) #基于梯度的分水img
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(camera_man, cmap="gray", imgpolation='nearest')
ax0.set_title("Original")
ax1.imshow(gradient, cmap="gray", interpolation='nearest')
ax1.set_title("Gradient")
ax2.imshow(markers, cmap="gray", interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap="gray", interpolation='nearest')
ax3.set_title("Segmented")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()