#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/24 01:25

import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path = "/Users/zhangyan/Desktop/IMG_7901.JPG"
img = cv2.imread(img_path)

# 代表读取的图像是会读图
img_gray = cv2.imread("/Users/zhangyan/Desktop/IMG_7901.JPG",cv2.IMREAD_GRAYSCALE)


# print(img_gray)
#
# show the picture on window
def show_picture(name,img):
    cv2.imshow(name, img)
    cv2.waitKey(0) # 设置任意键终止图片展示
    cv2.destroyAllWindows()
    # cv2.imwrite('/Users/zhangyan/Desktop/IMG_7901.JPG', img1) # save picture
#
#
# print(img.size)
# print(img.dtype)


# show_picture('gery', img_gray)


# video_path = "/Users/zhangyan/Desktop/sd1771774767_2.MP4"
# vc = cv2.VideoCapture(video_path)
#
# # 视频处理
# if vc.isOpened():
#     open,frame = vc.read()
# else:
#     open = False
#
# while open:
#     ret, frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow(video_path,gray)
#         # 0xFF== 27相当于快捷结束键，按esc结束视屏播放
#         if cv2.waitKey(10) & 0xFF== 27:
#             break
# vc.release()
# cv2.destroyAllWindows()


# 截取部分头像

# img1 = cv2.imread(img_path)
# cat = img1[0:50,0:200]
# show_picture("pic",cat)

img2_path = "/Users/zhangyan/Desktop/IMG_8675.JPG"
img2 = cv2.imread(img2_path)
# b,g,r = cv2.split(img2)
# print(r)
# print(r.shape)

# # 合并b,g,r三颜色通道
# img3 = cv2.merge((b,g,r))
# print(img3.shape)

# 只展示blue
copy_img2 = img2.copy()
# copy_img2[:,:,1] = 0
# copy_img2[:,:,2] = 0
# show_picture('tree',copy_img2)

# only show R
# copy_img2[:,:,0] = 0
# copy_img2[:,:,1] = 0
# show_picture('tree',copy_img2)

# only show G
# copy_img2[:,:,0] = 0
# copy_img2[:,:,2] = 0
# show_picture('tree',copy_img2)


# border added 边界填充

top_size,bottom_size,left_size,right_size = (100,100,100,100)

# 复制法填充边界
replicate = cv2.copyMakeBorder(img2,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
# 反射法填充边界
reflect = cv2.copyMakeBorder(img2,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)
# 反射法填充边界
reflect101 = cv2.copyMakeBorder(img2,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101)
# 常数填充法
wrap = cv2.copyMakeBorder(img2,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)
# 常数填充法
constant = cv2.copyMakeBorder(img2,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=0)


plt.subplot(231),plt.imshow(img2,'gray'), plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'), plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'), plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'), plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'), plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'), plt.title('constant')

# plt.show()

# 图像数值计算

img_tree = cv2.imread("/Users/zhangyan/Desktop/IMG_8675.JPG")
img_light = cv2.imread("/Users/zhangyan/Desktop/IMG_7901.JPG")

img_tree1 = img_tree + 10  # 直接加数字
# print(img_tree1[:5,:,0])
# print(img_tree[:5,:,0])

# 两个图片数值相加，超过的时候会取余数展示出来
merge1 = (img_tree+img_light)[:5,:,0]
# print(img_tree[:5,:,0])
# print(img_light[:5,:,0])
# print(merge1)

# 两个图片数值相加，超过的时候直接展示最大值，超过255会直接展示255。
merge2 = cv2.add(img_tree,img_light)[:5,:,0]
# print(merge2)

# image merge

print(img_tree.shape)
print(img_light.shape)

resize_img_tree = cv2.resize(img_tree,(0,0),fx=1,fy=3)  # 自己设定倍数关系
# show_picture('1',resize_img_tree)

# 合并图片
merge3 = cv2.addWeighted(img_tree,0.6,img_light,0.4,0) # 将两张图片融合在一起，设置图片的权重，调整亮度集
show_picture('1',merge3)














