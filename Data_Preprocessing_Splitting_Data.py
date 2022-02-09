# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:36:26 2022

@author: SUTD
"""
#%%
import os
import shutil

input_path = 'C:/Rajesh/XCT Dataset/Raw_Samples_2_6/set1sample2raw'
output_path = 'C:/Rajesh/XCT Dataset/Raw_Samples_2_6/splitted_folder'

'''remove existing output folder'''
if os.path.exists(output_path):
    shutil.rmtree(output_path)

else:
    '''file not found message'''
    print("File not found in the directory")
    
'''creating new output directory'''
os.mkdir(output_path)
#%%
''' splitting the images in the folder into the respective ratio'''
'''install spli-folders using below comment if not installed already'''
# !pip install split-folders

import splitfolders

train_ratio = 0.7
valid_ratio = 0.2
test_ratio = 0.1
splitfolders.ratio(input_path, output=output_path, seed=1000, 
                   ratio=(train_ratio, valid_ratio, test_ratio),group_prefix=None)
print(' ratio=({:.2f} train, {:.2f} valid, {:.2f} test)'.format(train_ratio, valid_ratio, test_ratio))

'''defining train, test, val folder path'''
train_path = output_path + '/train/'
test_path = output_path + '/test/'
val_path = output_path + '/val/'
#%%
'''calculating the number of images in the folder'''
import glob
train_count = len(glob.glob(train_path+'**/*.tif'))
test_count = len(glob.glob(test_path+'**/*.tif'))

print("train_count:", train_count, "test_count:", test_count)
#%%
'''# Identifying number of classes inside the training dataset'''
import pathlib
root=pathlib.Path(train_path)
classes=sorted([j.name.split('/')[-1] for j in root.iterdir()])
print(classes)
num_classes = len(classes)
print("num_classes:", num_classes)
#%%