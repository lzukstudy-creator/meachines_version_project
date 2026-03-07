#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/4 23:32
import cv2
import numpy as np
from PIL import Image
import pytesseract
from open_cv_basic_function import show_pic

# 将图片等比例缩小
def resize(image,width=None,height=None,inter=cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height/float(h)
        dim = (int(w*r),height)
    else:
        r = width/float(w)
        dim = (width,int(h*r))
    resized = cv2.resize(image,dim,interpolation=inter)
    return resized

def order_point(pts):
    rect = np.zeros((4,2),dtype="float32")
    # 计算左上，右下
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts,axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect


def four_point_transform(image,pts):
    rect = order_point(pts)
    (tl,tr,br,bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0,0],
        [maxWidth-1,0],
        [maxWidth-1,maxHeight-1],
        [0,maxHeight-1]],dtype='float32')
    M = cv2.getPerspectiveTransform(rect,dst)
    warped = cv2.warpPerspective(image,M,(maxWidth,maxHeight))
    return warped

img_path = "/Users/zhangyan/Desktop/pic/IMG_9954.JPG"
img = cv2.imread(img_path)
ratio = img.shape[0]/500
orgi = img.copy()

# 获取缩小至500的比例
image = resize(orgi,height = 500)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_gaussian = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(gray_gaussian,75,200)

# show_pic(edged,"edged")

cnts = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]
cnts_sort = sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
# print(cnts_sort)

for c in cnts_sort:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri,True)

    if len(approx) == 4:
        screenCnt = approx
        break

# step2 获取轮廓(最好提前判断一下不是None，要不可能会报错)
if screenCnt is not None:
    # 第一步：准备一张“画布”（通常是你的原图副本）
    canvas = image.copy()

    # 第二步：把坐标点“描”在画布上
    # 参数含义：在canvas上画，画screenCnt这个轮廓，画所有点(-1)，绿色(0,255,0)，粗细为3
    cv2.drawContours(canvas, [screenCnt], -1, (0, 255, 0), 3)

    # 第三步：展示这张画好了线的图
    show_pic(canvas, "Result_with_Contour")
else:
    print("没找到小票，screenCnt 是空的，所以没法画！")

warped = four_point_transform(orgi,screenCnt.reshape(4,2)*ratio)

warped_img = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
ref = cv2.threshold(warped_img,100,255,cv2.THRESH_BINARY)[1]
cv2.imwrite('/Users/zhangyan/Desktop/scan1.jpg',ref) # 需要绝对路径去保存图片

cv2.imshow("original",resize(orgi,height=650))
cv2.imshow("scanned",resize(ref,height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()



