#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/7 23:18

import cv2
import numpy as np
from PIL import Image
import pytesseract
from open_cv_basic_function import show_pic

img = cv2.imread("/Users/zhangyan/Desktop/pic/IMG_9306.JPG")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp = sift.detect(gray,None)

img1 = cv2.drawKeypoints(gray,kp,img)
# show_pic(img1,'img1')

kp ,des =sift.compute(gray,kp)
# print(np.array(kp).shape)
# print(des.shape)
print(des[0])














