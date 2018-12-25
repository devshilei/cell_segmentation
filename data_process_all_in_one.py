#coding:utf-8
"""
Created on 2018年12月21日

@author: devshilei@gmail.com
"""
import shutil
root_path = "D:/Mimage/12-21"
source_file_name_list = []
import os
for root, dirs, files in os.walk(root_path):
    for name in files:
        if "Thumbs.db" != name and name[0] != "X":
            full_path = os.path.join(root, name)
            rename = full_path.replace("D:/Mimage/", "").replace("\\", "_")
            target_file_path = os.path.join("image_files", rename)
            print(full_path, target_file_path)
            shutil.copyfile(full_path, target_file_path)