#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/1 23:15


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

magnitude = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img,cmap="gray")
plt.title("input image"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude,cmap="gray")
plt.title("magnitude"),plt.xticks([]),plt.yticks([])
plt.show()




