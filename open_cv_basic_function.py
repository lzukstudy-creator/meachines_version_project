#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/27 22:25

import cv2


def show_pic(path,name):
    cv2.imshow(name,path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

