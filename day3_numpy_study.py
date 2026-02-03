#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/2/2 01:58


import numpy as np


# arange have three 元素（start,stop,step）
# 包开始不包结束列：s:1,e:10,最终结果没有10， 返回是整型的int
a = np.arange(20)
b = np.arange(1,20)
c = np.arange(0,10,2)
d = np.arange(10000)
e = np.arange(10,step=2)

# linspace是求等差数列的
# parameter: start,end,num=default:50,endpoint=default:True,retstep=default:False,dtype
# 默认输出是浮点型
f = np.linspace(1,10,5)
g = np.linspace(1,10) # 默认50
h = np.linspace(1,10,5,endpoint=False)
i = np.linspace(1,10,5,retstep=True) # The result will show common difference is
j = np.linspace(1,10,5,dtype=None)


# logspace是求等比数列的
# parameter: start,end,num=default:50,endpoint=default:True,base:log的底数,dtype
# 默认输出是浮点型
k = np.logspace(1,10,5,base=5) # 取5的1-10次方
l = np.logspace(1,10,base=2) # 默认50个
m = np.logspace(1,10,base=2,endpoint=False)# 不包含10
n = np.logspace(1,10,5)
o = np.logspace(1,10,5,dtype=None)


# 全零数组 parameter:shape(形状几行几列), dtype默认float，int需要自己定义

p = np.zeros((5,))
q = np.zeros((2,2),dtype='int') # 转成整型需要定义
r = np.zeros((3,3)) # 2维
s = np.zeros((3,3,3)) # 3行3列 3维的
t = np.array([[1,2,3],[4,5,6]])
u = np.zeros_like(t)


# 全一数组 parameter:shape(形状几行几列), dtype默认float，int需要自己定义

v = np.ones((5,))
w = np.ones((2,2),dtype='int') # 转成整型需要定义
x = np.ones((3,3)) # 2维
y = np.ones((3,3,3)) # 3行3列 3维的
z = np.array([[1,2,3],[4,5,6]])
a1 = np.ones_like(t)
# print(f.ndim)



# 常用参数 shape, reshape,resize, ndim, size,dtype, itemsize

# print(z.shape) # 返回数据几行几列
# print(a.reshape((4,5))) # 改变数字的行列布局，但是不能改变超过20的数量
# print(np.resize(z,(2,4))) # 适用于新数组大于原数组，递归方式展示数据
# print(y.ndim) # 秩，展示数据是几维数组
# print(y.size) # 展示数组元素总个数
# print(y.dtype) # 展示数组元素对象类型
# print(y.astype('int').dtype) # 修改数组元素对象类型
# print(y.itemsize) # 字节显示每一个元素的大小







