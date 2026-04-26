#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/8 01:24

import cv2
import numpy as np
from PIL import Image
import pytesseract
from open_cv_basic_function import show_pic

img1 = cv2.imread("/Users/zhangyan/Desktop/pic/room01.jpeg",0)
img2 = cv2.imread("/Users/zhangyan/Desktop/pic/room02.jpeg",0)

sift = cv2.SIFT_create()
kp1,des1 = sift.detectAndCompute(img1,None)
kp2,des2 =sift.detectAndCompute(img2,None)

# bf = cv2.BFMatcher(crossCheck=True)
#
# matches = bf.match(des1,des2)
# matches_sorted = sorted(matches,key=lambda x:x.distance)
#
# img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
# show_pic(img3,"matches")

# k对最佳匹配
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
print(matches)
good = []

for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
show_pic(img3,"img3")



# sift = cv2.SIFT_create()
#
# kp1, des1 = sift.detectAndCompute(img1,None)
# kp2, des2 = sift.detectAndCompute(img2,None)
#
# bf = cv2.BFMatcher()
#
# matches = bf.knnMatch(des1,des2,k=2)
#
# good = []
# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append(m)
#
# src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
# dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
#
# H,mask = cv2.findHomography(src_pts,dst_pts,cv2.RANSAC,5.0)
#
# matchesMask = mask.ravel().tolist()
#
# img3 = cv2.drawMatches(
#     img1,kp1,
#     img2,kp2,
#     good,None,
#     matchesMask=matchesMask,
#     flags=2
# )
#
# show_pic(img3,"matches")
