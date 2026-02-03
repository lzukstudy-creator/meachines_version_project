#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2025/12/23 00:21


import numpy as np
import matplotlib.pyplot as plt

# arange 可以创建从0开始的一个C语言为基础的数组，且计算速度比Python循环更快
# numpy 是专门处理数据的

def numpy_count(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = np.arange(10)
    print(a + b)
    print(c)

def python_achieve_count(n):
    a = [i**2 for i in range(n)]
    b = [i**3 for i in range(n)]
    sum_answer = []
    for i in range(n):
        sum_answer.append(a[i]+b[i])
    print(sum_answer)

# ndarray数组是一个n维数组对象，只能存储同一类型的数组集合
p = np.array([1.1, 2, 3.8, 4, 5], dtype='int')
# print(p)
o = np.array([1,2,3,4,5], dtype="float")
# print(o)
u = np.array(list[[1,2,3,4],('a','b','c','d')])
# print(u)

a = np.array([1,2,3,4,5])
b = np.array(a)
print('id:', id(a),'id',id(b))
a[0] = 10
print(a,b)

a = np.array([[1,2,3],
             [1,2,3]])

img = np.zeros((100, 300, 3), dtype=np.uint8)

img[:, 0:100] = [255, 0, 0]    # 红
img[:, 100:200] = [0, 255, 0]  # 绿
img[:, 200:300] = [0, 0, 255]  # 蓝


def show_slices(step=4):
    """
    step 越小颜色越细腻，但图片越大、渲染越慢。
    推荐：step=4 或 step=8
    """
    vals = np.arange(0, 256, step, dtype=np.uint8)
    n = len(vals)

    # 固定 B，展示 (R,G) 平面：每一张图就是一个“切片”
    B_levels = [0, 64, 128, 192, 255]

    fig, axes = plt.subplots(1, len(B_levels), figsize=(16, 3))
    for ax, B in zip(axes, B_levels):
        # 生成一个 n x n 的图，每个像素是 (R,G,B)
        img = np.zeros((n, n, 3), dtype=np.uint8)
        # 横轴 R，纵轴 G
        img[:, :, 0] = vals[np.newaxis, :]      # R
        img[:, :, 1] = vals[:, np.newaxis]      # G
        img[:, :, 2] = B                        # B 固定

        ax.imshow(img)
        ax.set_title(f"B = {B}")
        ax.set_xlabel("R →")
        ax.set_ylabel("G ↑")
        ax.set_xticks([])
        ax.set_yticks([])

    plt.suptitle("RGB Cube Slices (fix B, vary R & G)")
    plt.tight_layout()
    plt.show()


def rgb_cube_3d(step=16):
    """
    step 越小点越多越慢：
    step=16 大概 16^3=4096 点（推荐）
    step=8  大概 32^3=32768 点（可能略慢）
    """
    vals = np.arange(0, 256, step, dtype=np.uint8)
    R, G, B = np.meshgrid(vals, vals, vals, indexing="ij")

    r = (R.flatten() / 255.0)
    g = (G.flatten() / 255.0)
    b = (B.flatten() / 255.0)

    colors = np.stack([r, g, b], axis=1)

    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(r, g, b, c=colors, s=20, depthshade=False)

    ax.set_xlabel("R")
    ax.set_ylabel("G")
    ax.set_zlabel("B")
    ax.set_title("RGB Cube (3D)")

    plt.show()


# -- --------------------------- #
a1 = np.arange(4.1) # 可以输入浮点型创建列表
print(a1)

a2 = np.arange(5,dtype='float')
print(a2)

a3 = np.arange(10,20,2)
print(a3)

a4 = np.arange(10,20,3)
print(a4)


# if __name__ == "__main__":
#     rgb_cube_3d(step=16)


# if __name__ == "__main__":
#     show_slices(step=4)





# numpy_count(10)
# print(python_achieve_count(10))
