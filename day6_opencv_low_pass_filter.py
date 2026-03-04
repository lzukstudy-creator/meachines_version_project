#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/1 23:33

from open_cv_basic_function import show_pic
import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path = "/Users/zhangyan/Desktop/pic/IMG_9707.JPG"
img = cv2.imread(img_path,0)  # 0 means transfer to gray img

# cv2.dft(),cv2.idft()
# when you do the dft, you must need float32 in img

img_float32 = np.float32(img)
dft = cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

row,col = img.shape
crow,ccol = int(row/2),int(col/2) # get center point

# low pass filter use np.zero make a mask, make mask center to 1
mask = np.zeros((row,col,2), np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30] = 1

# IDFT
fshift = dft_shift*mask
f_fshift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_fshift)
img_back1 = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img,cmap="gray")
plt.title("input image"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img_back1,cmap="gray")
plt.title("magnitude"),plt.xticks([]),plt.yticks([])
plt.show()






