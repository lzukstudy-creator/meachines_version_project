#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/28 22:26


from open_cv_basic_function import show_pic
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 轮廓检测
# step1 get thresh
img = cv2.imread("/Users/zhangyan/Desktop/pic/IMG_9875.JPG")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# show_pic(thresh,"thresh")

# step 2 get contours
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# step3 draw new pic
draw_img = img.copy()
res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
show_pic(res,"res")









