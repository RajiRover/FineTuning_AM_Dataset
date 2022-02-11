# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 19:59:09 2022

@author: SUTD
"""

from matplotlib import pyplot as plt
import shutil
import os
import cv2
import glob
import numpy as np

threshold_category = ['Otsu threshold', 'Adaptive_Mean', 'Adaptive_Gaussian']
samples = ['set1sample2raw', 'set1sample3raw', 'set1sample4raw', 'set1sample5raw', 'set1sample6raw']

threshold_value = []
thresh_image = []
# 
for thr in threshold_category:
    for pth in samples:    
        input_path = "C:/Rajesh/XCT Dataset/Raw_Samples_2_6/{}/*.tif".format(pth)
        output_folder = 'C:/Rajesh/XCT Dataset/Raw_Samples_2_6/ground_truth/{}/{}/'.format(thr, pth)
        
        if os.path.exists(output_folder):
            # removing the file using the os.remove() method
            shutil.rmtree(output_folder)
        else:
            # file not found message
            print("File not found in the directory")
        os.mkdir(output_folder)
        
        path = glob.glob(input_path)
        
        images = []
        
        for bb,img in enumerate(path):
        
            image = cv2.imread(img)
            
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(image_gray, (7,7), 0)
            
            histg = cv2.calcHist([blurred], [0], None, [255], [0,255])
            # plt.figure(2)
            # plt.hist(image_gray.flat, bins=100, range=(50,255))
            
            if thr == 'Otsu threshold':
                
                within = []
                
                for i in range(len(histg)):
                    x,y = np.split(histg, [i])
                    x1 = np.sum(x)/(image.shape[0]*image.shape[1])
                    y1 = np.sum(y)/(image.shape[0]*image.shape[1])
                    x2 = np.sum([ j*t for j,t in enumerate(x)])/np.sum(x)
                    x2 = np.nan_to_num(x2)
                    y2 = np.sum([ j*t for j,t in enumerate(y)])/np.sum(y)
                    y2 = np.nan_to_num(y2)
                    x3 = np.sum([ (j-x2)**2*t for j,t in enumerate(x)])/np.sum(x)
                    x3 = np.nan_to_num(x3)
                    y3 = np.sum([ (j-y2)**2*t for j,t in enumerate(y)])/np.sum(y)
                    y3 = np.nan_to_num(y3)
                    
                    within_min = x1*x3 + y1*y3
                    within.append(within_min)
                mini = np.argmin(within)
                # print(mini)
                threshold_value.append(mini)
                
                ret, thresh = cv2.threshold(blurred, mini, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                # plt.figure(2)
                # plt.imshow(thresh, cmap='gray')
                cv2.imwrite(output_folder + 'image_{}.tif'.format(bb), thresh)
            
            elif thr == 'Adaptive_Mean':
                thresh1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 12)
                # plt.figure(3)
                # plt.imshow(thresh1, cmap='gray')
                cv2.imwrite(output_folder + 'image_{}.tif'.format(bb), thresh1)
            
            elif thr == 'Adaptive_Gaussian':
                thresh2 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 19, 12)
                # plt.figure(4)
                # plt.imshow(thresh2, cmap='gray')
                cv2.imwrite(output_folder + 'image_{}.tif'.format(bb), thresh2)
           
            else:
                print("Gorund truth images are generated")
    




