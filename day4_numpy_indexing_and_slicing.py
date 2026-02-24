#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/3 00:16

import numpy as np
import cv2

print(cv2.__version__)


# 索引和切片，索引是从0开始，所以数数的时候下标要+1。-1代表最后一位

# 一维数组索引和切片
rg1 = np.array([1,2,3,4,5,6,7])
print(rg1)
# 取2-6的数据
rg2 = rg1[1:7] #从前往后取
rg3 = rg1[:-1:1] # 从最后一位往前取-1代表最后一位，起始第一位为0
print(rg2)
rg4 = rg1[2] # 直接取某一位的数值
print(rg4)

# 二维数组索引和切片，先取一维数组的行，在取具体某个数组或多个数组的下标
# tips：包前不包后，切片的时候前面包含后面不包含
rg5 = np.arange(20).reshape(4,5)
rg6 = rg5[0][1:4] # 取第一行的中间三位
print(rg5)
print(rg6)
rg7 = rg5[:-2] # 取前两列
print(rg7)
rg8 = rg5[:-2][1]# 取前两行中的第二行
print(rg8)
rg9 = rg5[:-2][1][1:3]# 取前两行中的第二行的第2个和第3个
print(rg9)

# 索引高级操作
rg10 = np.arange(20).reshape(4,5)
print(rg10)
# 取所有行第二列的数据，在一个括号中输入内容，前面输入的是行，后面输入的是列.省略号...代表所有
rg11 = rg10[...,1]
print(rg11)
rg12 = rg10[...,1:] # 取所有行，从第2列开始包含第二列的所有元素
print(rg12)

# 高级索引操作2
num = np.array([[0,1,2],
                [3,4,5],
                [6,7,8],
                [9,10,11]])

num1 = num[[0,0,3,3],[0,2,0,2]]

r = np.array([[0,0],[3,3]]).reshape(4)













