#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/28 21:16

from open_cv_basic_function import show_pic
import cv2
import matplotlib.pyplot as plt
import numpy as np

# matchTemplate
# 模版匹配
img1 = cv2.imread("/Users/zhangyan/Desktop/pic/IMG_9707.JPG")
template =cv2.imread("/Users/zhangyan/Desktop/pic/WechatIMG791.jpg")
h,w = template.shape[:2]
print(template.shape)
print(img1.shape)

res = cv2.matchTemplate(img1,template,cv2.TM_CCOEFF_NORMED)
print(res.shape)

min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0]+w,top_left[1]+h)
pic1 = cv2.rectangle(img1,top_left,bottom_right,(0,0,255),10)
cv2.imshow("img",pic1)
cv2.waitKey(0)
cv2.destroyAllWindows()


















