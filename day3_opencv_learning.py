#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/25 20:58

import cv2
import matplotlib.pyplot as plt
import numpy as np

# exp: ret, dst = cv2.threshold(src,thresh,maxval,type)
# 二值法取数据 First one is img path
# Second one is minimum, if the value small than Second, so it will be changed to Second
# Maxval is Maximum, when vaule overtake max, it will be changed to max
# type is what you want show

img = cv2.imread("/Users/zhangyan/Desktop/IMG_8675.JPG")

ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY', 'BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
# plt.show()



# slove the image noise

img2 = cv2.imread("/Users/zhangyan/Desktop/IMG_8675.JPG")
cv2.imshow('img',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = cv2.imread("/Users/zhangyan/Desktop/2.jpg")

blur1 = cv2.blur(img3,(3,3))  # 均值滤波
# cv2.imshow('img',img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

box = cv2.boxFilter(img3,-1,(3,3),normalize=False)  # 方框滤波
# cv2.imshow('img',img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

aussian = cv2.GaussianBlur(img3,(5,5),1)  # 高斯滤波
# cv2.imshow('img',img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

median = cv2.medianBlur(img3,5)  # 中值滤波
# cv2.imshow('img',img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

merge = np.hstack((blur1,aussian,median))  # 合并横屏展示三种处理后的图片
cv2.imshow('img',merge)
cv2.waitKey(0)
cv2.destroyAllWindows()











