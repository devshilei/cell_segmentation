#coding:utf-8
"""
Created on 2018年12月25日
@author: devshilei@gmail.com
"""
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("demo/3.jpg")
print(img.getpixel((50,100)))
print(type(img))
print(img.size)           #图片的尺寸
print(img.mode)           #图片的模式
print(img.format)         #图片的格式
print(img.getpixel((0,0)))#得到像素：
#img读出来的图片获得某点像素用getpixel((w,h))可以直接返回这个点三个通道的像素值
gray = img.convert("L")
# r, g, b = img.split()
# fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(8, 3), sharey=True)
# ax = axes.ravel()
# ax[0].imshow(img)
# ax[0].set_title('Origin image')
# ax[0].set_xticks([]), ax[0].set_yticks([])
# ax[1].imshow(gray, cmap="gray")
# ax[1].set_title("Gray image")
# ax[1].set_xticks([]), ax[1].set_yticks([])
# ax[2].imshow(gray.convert('1'), cmap="gray", interpolation='nearest')
# ax[2].set_title("Binary image")
# ax[2].set_xticks([]), ax[2].set_yticks([])
# ax[3].imshow(img.convert('CMYK'), interpolation='nearest')
# ax[3].set_title("CMYK image")
# ax[3].set_xticks([]), ax[3].set_yticks([])
# ax[4].imshow(img.convert('I'), interpolation='nearest')
# ax[4].set_title("I image")
# ax[4].set_xticks([]), ax[4].set_yticks([])
# ax[5].imshow(img.convert('F'), interpolation='nearest')
# ax[5].set_title("F image")
# ax[5].set_xticks([]), ax[5].set_yticks([])
# ax[6].imshow(r, cmap="rainbow", interpolation='nearest')
# ax[6].set_title("R image")
# ax[6].set_xticks([]), ax[6].set_yticks([])
# ax[7].imshow(g, cmap="rainbow", interpolation='nearest')
# ax[7].set_title("G image")
# ax[7].set_xticks([]), ax[7].set_yticks([])
# ax[8].imshow(b, cmap="rainbow", interpolation='nearest')
# ax[8].set_title("B image")
# ax[8].set_xticks([]), ax[8].set_yticks([])

# plt.figure("Neural Network")
# plt.figure(num=1, figsize=(8,5),)
# plt.title("The image title")
# plt.axis("off") # 不显示坐标轴
# plt.imshow(img)
# plt.show()

# img2 = Image.open("demo/2.jpg")
# img_blend = Image.blend(img, img2, alpha=.7)
# img_blend.save("demo/img_2_3_blend.jpg")
# mask = img2.convert("L")
# img_composite = Image.composite(img, img2, mask)
# img_composite.save("demo/img_2_3_composite.jpg")


import numpy as np
# 将 PIL Image 图片转换为 numpy 数组
im_array = np.array(img)
# 也可以用 np.asarray(im) 区别是 np.array() 是深拷贝，np.asarray() 是浅拷贝

# #随机生成5000个椒盐
# rows,cols,dims=im_array.shape
# for i in range(5000):
#     x=np.random.randint(0,rows)
#     y=np.random.randint(0,cols)
#     im_array[x,y,:]=255
#     
plt.figure("beauty")
plt.imshow(gray, cmap="gray")
plt.axis('off')
plt.show()
from collections import Counter

gray_array = np.array(gray)
split_array = np.array(gray_array[:418,:1430], dtype=np.int32)
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(4, 3), sharey=True)

print(np.min(split_array), np.max(split_array), np.average(split_array))
split_array[split_array>224] = 0
print(np.min(split_array), np.max(split_array), np.average(split_array))
# plt.imshow(split_array, cmap="gray")
ax = axes.ravel()
ax[0].imshow(np.array(img)[:418,:1430])
ax[0].set_title('Origin image')
ax[0].set_xticks([]), ax[0].set_yticks([])

ax[1].imshow(gray_array[:418,:1430], cmap="gray")
ax[1].set_title("Gray image")
ax[1].set_xticks([]), ax[1].set_yticks([])

ax[2].imshow(split_array, cmap="gray", interpolation='nearest')
ax[2].set_title("Binary image")
ax[2].set_xticks([]), ax[2].set_yticks([])

num=1000000
lst = np.random.randint(num / 10, size=num)
print(type(lst), lst.dtype, lst.shape)
res = Counter(lst) 
print(type(res))
# 输出的是出现次数最后的数据如[('xxx', 8), ('xxx', 5),]
print(type(split_array), split_array.dtype, split_array.shape)
split_array_counter = Counter(split_array.flatten())
print(type(split_array_counter), split_array_counter.most_common(30))
# Counter(words).most_common(4)    
plt.show()