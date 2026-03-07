#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/7 00:18

import cv2
import numpy as np
from PIL import Image
import pytesseract
from open_cv_basic_function import show_pic

img = cv2.imread("/Users/zhangyan/Desktop/pic/carwash.jpg")
print("img.shape",img.shape)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(img_gray,15,3,0.02)
print("dst.shape",dst.shape)

img[dst>0.01*dst.max()] = [0,0,255]
show_pic(img,"img")











