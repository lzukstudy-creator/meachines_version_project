#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/27 22:24

from open_cv_basic_function import show_pic
import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path = "/Users/zhangyan/Desktop/pic/IMG_9707.JPG"
img_read = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
# Studying a method of Sobel function to get picture's Edge Detection.
# 边缘检测

# Just show the Left side picture when you show a circle
# Working on x, use right - left, get part of left circle
# cv2.CV_64F is for show the picture perfect
# 当没有使用绝对值的时候，展示的数据只有一半，由于是右边-左边，切最小值为0，所以右边展示为黑色
sobelx = cv2.Sobel(img_read,cv2.CV_64F,1,0,ksize=3)
# show_pic(sobelx,"sobelx")

# If we need a whole circle, we need add get a positive count
# exp: |-1| = 1
# 取绝对值，获得整个圆
convert = cv2.convertScaleAbs(sobelx)
# show_pic(convert,"convert")

# 如果我想从y轴获取这个边缘，则是下-上，取绝对值，也会得到一个圆
# If i want to get a Y circle, it will use |bottom - top| to get a whole circle
sobely = cv2.Sobel(img_read,cv2.CV_64F,0,1,ksize=3)
convert1 = cv2.convertScaleAbs(sobely)
# show_pic(convert1,"convert")

# get whole Circle without lose through merge x and y
# 获取整个圆的边缘，通过合并x和y的取值,要绝对值的数据
sobelxy = cv2.addWeighted(convert,0.5,convert1,0.5,0)
# show_pic(sobelxy,"sobelxy")


# remember tips: if you want to get pic sobely, you should calculate x and y separate
# then you can get a good pic, Do NOT calculate x and y on one function

# 计算的时候，最好是先分开计算x和y的绝对值，不要一起计算
# sobelx = cv2.Sobel(img_read,cv2.CV_64F,1,1,ksize=3) Do Not use 1,1.


# different fuction to get pic's Edge Detection.
# 其他不同方法的边缘检测

# Scharr function
scharrx = cv2.Sobel(img_read, cv2.CV_64F, 1, 0, ksize=3)
scharry = cv2.Sobel(img_read,cv2.CV_64F,0,1,ksize=3)
convert3 = cv2.convertScaleAbs(scharrx) # get |Scharrx|
convert4 = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(convert3, 0.5, convert4, 0.5, 0)

# Laplacian function
laplacian = cv2.Laplacian(img_read,cv2.CV_64F)
convert5 = cv2.convertScaleAbs(laplacian)

res = np.hstack((sobelxy,scharrxy,convert5))
# show_pic(res,'res')

# Canny function to get pic's Edge
# different maxVal and minVal will get different pic
v1 = cv2.Canny(img_read,80,150)
v2 = cv2.Canny(img_read,50,100)
res1 = np.hstack((v1,v2))
show_pic(res1,'res1')









