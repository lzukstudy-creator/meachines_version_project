#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/1 22:00


from open_cv_basic_function import show_pic
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = "/Users/zhangyan/Desktop/pic/IMG_9707.JPG"
read_img = cv2.imread(img,0)  # 0 means transfer to gray img

# cv2.calcHist
# 1.[img] 2.[] is channels count
# 3.mask None means no Mask
# 4.histSize usual [256]
# 5.ranges usual [0,256]
# must need [] or will mistake when program running

# hist = cv2.calcHist([read_img],[0],None,[256],[0,256])
# # print(hist.shape)
# --->(256,1) means between 0-255,1 means is a 2D

plt.hist(read_img.ravel(),256)
# # plt.show()

# this way can show the BGR frequency
img1 = cv2.imread(img)
color = ('b','g','r') # need follow the opencv rules:b,g,r
for i,col in enumerate(color):
    hist1 = cv2.calcHist([img1], [i], None, [256], [0, 256])
    plt.plot(hist1,color=col)
    plt.xlim([0,256])
# plt.show()


# Mask
# img1.shape[:2] it means ignore channel, because mask is a single channel
# np.uint8 it means only show 0-255
mask = np.zeros(read_img.shape[:2],np.uint8)
mask[100:1000,100:1300] = 255 # make mask shape, make to white
# show_pic(mask,"mask")

masked_img = cv2.bitwise_and(read_img,read_img,mask=mask)
# show_pic(masked_img,"masked_img")

# cv2.equalizeHist
equ = cv2.equalizeHist(read_img)
plt.hist(equ.ravel(),256)
# plt.show()
two = np.hstack((equ,read_img))
# # show_pic(two,"two")

# auto equalizeHist
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
res_clahe = clahe.apply(read_img)
res = np.hstack((read_img,equ,res_clahe))
# show_pic(res,"res")














