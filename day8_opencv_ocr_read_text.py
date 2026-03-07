#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/6 23:25

import cv2
import numpy as np
from PIL import Image
import pytesseract
from open_cv_basic_function import show_pic


img = cv2.imread("/Users/zhangyan/Desktop/pic/scan1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_blur = cv2.medianBlur(gray,3)
pil_img= Image.fromarray(gray_blur)

text = pytesseract.image_to_string(pil_img,lang="chi_sim")

print(text)















