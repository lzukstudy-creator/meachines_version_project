#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/25 23:10

import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path = "/Users/zhangyan/Desktop/WechatIMG777.jpg"
img_path2 = "/Users/zhangyan/Desktop/WechatIMG780.jpg"

# 腐蚀操作，去掉多余信息，cv2.erode
img = cv2.imread(img_path)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=1) # iterations once

# 腐蚀一个圆 cv2.erode
img2 = cv2.imread(img_path2)
kernel1 = np.ones((30,30),np.uint8)
erosion1 = cv2.erode(img2,kernel1,iterations=1)
erosion2 = cv2.erode(img2,kernel1,iterations=2)
erosion3 = cv2.erode(img2,kernel1,iterations=3)
res = np.hstack((erosion1,erosion2,erosion3))

# 膨胀操作 cv2.dilate
# 先腐蚀
img3 = cv2.imread(img_path)
kernel = np.ones((3,3),np.uint8)
erosion4 = cv2.erode(img3,kernel,iterations=1) # iterations once
# 在膨胀
dlig_dilate = cv2.dilate(erosion4,kernel,iterations=1)

# 膨胀一个圆
img2 = cv2.imread(img_path2)
kernel1 = np.ones((30,30),np.uint8)
erosion1 = cv2.dilate(img2,kernel1,iterations=1)
erosion2 = cv2.dilate(img2,kernel1,iterations=2)
erosion3 = cv2.dilate(img2,kernel1,iterations=3)
res1 = np.hstack((erosion1,erosion2,erosion3))

# Open - erode First, dilate Second
# 开运算（合并了两种方法，按先腐蚀在膨胀的顺序）
# cv2.morphologyEx--cv2.MORPH_OPEN

img3 = cv2.imread(img_path)
kernel2 = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img3,cv2.MORPH_OPEN,kernel2)


# Close - dilate First, erode Second
# 闭运算（合并了两种方法，按先膨胀在腐蚀的顺序）
# cv2.morphologyEx--cv2.MORPH_CLOSE
closing = cv2.morphologyEx(img3,cv2.MORPH_CLOSE,kernel2)


# 梯度运算 膨胀-腐蚀 dliate - erode cv2.MORPH_GRADIENT
# 得到的就是一个边缘，膨胀的部分减去腐蚀的部分，剩下的部分

img4 = cv2.imread(img_path2)
kernel3 = np.ones((7,7),np.uint8)
gradient = cv2.morphologyEx(img4,cv2.MORPH_GRADIENT,kernel3)


# Tophat 礼帽 cv2.MORPH_TOPHAT
# Tophat = 原始输入-开运算 start-(erode First, dilate Second)

img5 = cv2.imread(img_path)
top_hat = cv2.morphologyEx(img5,cv2.MORPH_TOPHAT,kernel)

# Blackhat 礼帽 cv2.MORPH_BLACKHAT
# Tophat = 原始输入-开运算 start-(erode First, dilate Second)

black_hat = cv2.morphologyEx(img5,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow('black_hat',black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()


