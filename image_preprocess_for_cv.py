#coding:utf-8
"""
Created on 2018年12月24日

@author: devshilei@gmail.com
"""
import os
import numpy as np
import cv2
# import matplotlib.pyplot as plt
#主函数
if __name__ =="__main__":
    root_path = "real/step_02_2_augmentation"
    target_path = "real/step_03_2_mask"
    filename_list = os.listdir(root_path)
    for filename in filename_list:
        full_path = os.path.join(root_path, filename)
        img = cv2.imread(full_path)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        lower, upper = np.array([156, 43, 46]), np.array([180, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        #inverse = cv2.bitwise_not(mask)
        output_image_filepath = os.path.join(target_path, filename.replace(".", "_mask."))
        cv2.imwrite(output_image_filepath, mask)
    print("finished".center(50, "-"))
#     fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 3), sharey=True)
#     ax = axes.ravel()
#     
#     ax[0].imshow(img)
#     ax[0].set_title('Origin image')
#     ax[0].set_xticks([]), ax[0].set_yticks([])
#     ax[1].imshow(hsv, cmap="gray")
#     ax[1].set_title("HSV image")
#     ax[1].set_xticks([]), ax[1].set_yticks([])
#     ax[2].imshow(mask, cmap="gray")
#     ax[2].set_title("Mask image")
#     ax[2].set_xticks([]), ax[2].set_yticks([])
#     ax[3].imshow(inverse, cmap="gray")
#     ax[3].set_title("Inverse image")
#     ax[3].set_xticks([]), ax[3].set_yticks([])
#     plt.show()