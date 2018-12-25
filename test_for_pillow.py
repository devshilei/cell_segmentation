#coding:utf-8
"""
Created on 2018年12月25日
@author: devshilei@gmail.com
"""
# from skimage import io, filters
#Image和skimage读图片
from PIL import Image, ImageDraw, ImageFont
# import os
import matplotlib.pyplot as plt

img = Image.open("3.jpg")
print(img.getpixel((50,100)))
print(type(img))
print(img.size)           #图片的尺寸
print(img.mode)           #图片的模式
print(img.format)         #图片的格式
print(img.getpixel((0,0)))#得到像素：
#img读出来的图片获得某点像素用getpixel((w,h))可以直接返回这个点三个通道的像素值

gray = img.convert('L')
r,g,b=img.split()
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(8, 3), sharey=True)
ax = axes.ravel()
ax[0].imshow(img)
ax[0].set_title('Origin image')
ax[0].set_xticks([]), ax[0].set_yticks([])
ax[1].imshow(gray, cmap="gray")
ax[1].set_title("Gray image")
ax[1].set_xticks([]), ax[1].set_yticks([])
ax[2].imshow(gray.convert('1'), cmap="gray", interpolation='nearest')
ax[2].set_title("Binary image")
ax[2].set_xticks([]), ax[2].set_yticks([])
ax[3].imshow(img.convert('CMYK'), interpolation='nearest')
ax[3].set_title("CMYK image")
ax[3].set_xticks([]), ax[3].set_yticks([])
ax[4].imshow(img.convert('I'), interpolation='nearest')
ax[4].set_title("I image")
ax[4].set_xticks([]), ax[4].set_yticks([])
ax[5].imshow(img.convert('F'), interpolation='nearest')
ax[5].set_title("F image")
ax[5].set_xticks([]), ax[5].set_yticks([])
ax[6].imshow(r, cmap="rainbow", interpolation='nearest')
ax[6].set_title("R image")
ax[6].set_xticks([]), ax[6].set_yticks([])
ax[7].imshow(g, cmap="rainbow", interpolation='nearest')
ax[7].set_title("G image")
ax[7].set_xticks([]), ax[7].set_yticks([])
ax[8].imshow(b, cmap="rainbow", interpolation='nearest')
ax[8].set_title("B image")
ax[8].set_xticks([]), ax[8].set_yticks([])

# plt.figure("Neural Network")
# plt.figure(num=1, figsize=(8,5),)
# plt.title("The image title")
# plt.axis("off") # 不显示坐标轴
# plt.imshow(img)
plt.show()


print("-" * 50)

# from skimage import io, transform
# img_file2 = io.imread("KG.jpg")
# #得到像素：
# print(img_file2[50][100])
# io.imshow(img_file2)
# print(type(img_file2))      #显示类型
# print(img_file2.shape)      #显示尺寸
# print(img_file2.shape[0])   #图片高度
# print(img_file2.shape[1])   #图片宽度
# print(img_file2.shape[2])   #图片通道数
# print(img_file2.size)       #显示总像素个数
# print(img_file2.max())      #最大像素值
# print(img_file2.min())      #最小像素值
# print(img_file2.mean())     #像素平均值
# print(img_file2[0][0])      #图像的像素值