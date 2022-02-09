# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:48:23 2022

@author: SUTD
"""


import numpy as np
from matplotlib import pyplot as plt
from patchify import patchify
import tifffile as tiff
import shutil
import os
from skimage.transform import resize

large_image_file = tiff.imread("C:/Rajesh/XCT Dataset/Raw_Samples_2_6/set1sample5raw/*.tif")
# resize_image = resize(large_image_file, (984,984,749))
output_folder = 'C:/Rajesh/XCT Dataset/Raw_Samples_2_6/Patches/Sample5_749images/'
if os.path.exists(output_folder):
    # removing the file using the os.remove() method
    shutil.rmtree(output_folder)
else:
    # file not found message
    print("File not found in the directory")
os.mkdir(output_folder)

for img in range(large_image_file.shape[0]):
    large_image = large_image_file[img]
    patch_img = patchify(large_image, (246, 246), step=246)
        
    for i in range(patch_img.shape[0]):
        for j in range(patch_img.shape[1]):
            single_patch_img = patch_img[i,j,:,:]
            tiff.imwrite(output_folder + 'image_' + str(img)+'_' + str(i)+str(j)+'.tif', single_patch_img)