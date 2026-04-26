#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/8 03:01

import cv2
import numpy as np
from PIL import Image
import pytesseract
from open_cv_basic_function import show_pic
from day9_opencv_image_merge import Stitcher

imageA = cv2.imread("/Users/zhangyan/Desktop/pic/room01.jpeg")
imageB = cv2.imread("/Users/zhangyan/Desktop/pic/room02.jpeg")

stitcher = Stitcher()

(result,vis) = stitcher.stitch([imageB,imageA],showMatches=True)

# cv2.imshow("imageA",imageA)
# cv2.imshow("imageA",imageB)
# cv2.imshow("KeyPoint",vis)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()


























