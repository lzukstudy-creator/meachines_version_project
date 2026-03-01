#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/28 22:48
import numpy

from open_cv_basic_function import show_pic
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 图像金字塔，等比例放大或者缩小图片
# pyr_img  pyrUp/pyrDown
img = cv2.imread("/Users/zhangyan/Desktop/pic/naturo.jpg")
# show_pic(img,"img")

# 放大图片 pyrUp
up = cv2.pyrUp(img)
# show_pic(up,"up")

# 放大图片 pyrUp twice
up2 = cv2.pyrUp(up)
# show_pic(up2,"up2")

# 缩小图片 pyrDown make pic small
down = cv2.pyrDown(img)
# show_pic(down,"down")

# let pic Up First then Down
# 图片会在放大和缩小过程中失去一些特征，导致图片变模糊
# The pic will lose some counts due to pic become Blurry
up3 = cv2.pyrUp(img)
up4 = cv2.pyrDown(up3)

show_two = numpy.hstack((img,up4))
# show_pic(show_two,"show_two")

# function2 拉普拉多金字塔  Lapuladuo

down1 = cv2.pyrDown(img)
down_up = cv2.pyrUp(down1)
# 使用此方法前一定要保证两个图片尺寸大小相同，否则会因为相减尺寸不一样报错
down_up = cv2.resize(down_up, (img.shape[1], img.shape[0]))
l_l = img-down_up
show_pic(l_l,'l_l')















