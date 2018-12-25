#coding:utf-8
"""
Created on 2018年12月25日
@author: devshilei@gmail.com
"""
import shutil
import os
from PIL import Image


def image_files_all_in_one(source_path, target_path):
    """
    Discription: 处理原始图像文件（汇总到一个文件目录下）
    @param source_path: 源目录
    @param target_path: 目标目录
    """
    for root, __, files in os.walk(source_path):
        for name in files:
            if "Thumbs.db" != name and name[0] != "X":
                full_path = os.path.join(root, name)
                rename = full_path.replace(source_path, "").replace("\\", "_")
                target_file_path = os.path.join(target_path, rename)
                print(full_path, target_file_path)
                shutil.copyfile(full_path, target_file_path)
    print("image_files_all_in_one".center(100, "-"))


def batch_image_resize(source_path, resized_file_path):
    """
    Discription: 原始文件几何变换：resize
    @param source_path: 源目录
    @param resized_file_path: 大小重置之后文件存储目录
    """
    file_name_list = os.listdir(source_path)
    for file_name in file_name_list:
        img = Image.open(os.path.join(source_path, file_name))
        (height, width) = img.size
        dst = img.resize((height, width))
        #half_height, half_width = height//2, width//2
        #print(file_name, height, width, half_height, half_width)
        #img.resize((half_height, half_width))
        dst.save(os.path.join(resized_file_path, file_name))
    print("batch_image_resize".center(100, "-"))


def image_augmentation(source_path, target_path):
    """
    Discription: 图像增广：原始文件几何变换：[包括上下、左右镜像、顺时针旋转180°]
    @param source_path: 源目录
    @param target_path: 几何变换后文件存储目录
    """
    file_name_list = os.listdir(source_path)
    for file_name in file_name_list:
        img = Image.open(os.path.join(source_path, file_name))
        dst = img.transpose(Image.FLIP_LEFT_RIGHT)  #左右互换
        dst.save(os.path.join(target_path, "FLR_" + file_name))
        dst = img.transpose(Image.FLIP_TOP_BOTTOM)  #上下互换
        dst.save(os.path.join(target_path, "FTB_" + file_name))
        dst = img.transpose(Image.ROTATE_180)       #顺时针旋转
        dst.save(os.path.join(target_path, "R180_" + file_name))
    print("image_augmentation".center(100, "-"))

if __name__ == '__main__':
#     # step1 将原始文件拷贝到统一文件目录下
#     source_path, target_path = "D:/Mimage/12-21", "images/step_01_all_in_one"
#     image_files_all_in_one(source_path, target_path)
#     # step2 原始文件重置大小
#     source_path, resized_file_path = "real/step_01_all_in_one", "real/step_02_1_resize"
#     batch_image_resize(source_path, resized_file_path)
#     source_path, target_path = "real/step_02_1_resize", "real/step_02_2_augmentation"
#     # step2-2 原始文件重置大小
#     image_augmentation(source_path, target_path)
    pass