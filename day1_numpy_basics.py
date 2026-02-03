#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2025/12/22 12:29 上午
import sys
import cv2, numpy as np
from decimal import Decimal, ROUND_HALF_UP

# Day 1 – NumPy Basics
# - Understand image as a NumPy array
# - Practice slicing (ROI)
# - Simulate grayscale and color images

# print("Python:", sys.version)
# print("NumPy:", np.__version__)
# print("OpenCV:", cv2.__version__)
# print("Python path:", sys.executable)


# def count_bmi():
#     input_weight = float(input("please input weight"))
#     input_height = float(input("please input height"))
#     count = Decimal(str(input_weight/input_height**2))
#     count_str = count.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
#     print(float(count_str))
#
# count_bmi()

#
# def getlen(x:str):
#     print(len(x))
#
# getlen("122321312")

class Solution:
    def longestConsecutive(self, nums) -> int:
        left = 0
        right = 1
        n = len(nums)
        s = set()
        while left < n:
            if right >= n:
                left +=1
                right = left+1
            elif abs(left-right) == 1 or abs(right-left) == 1:
                s.add(left)
                s.add(right)
        return len(s)

if __name__ == '__main__':
    solution = Solution()
    solution.longestConsecutive([100,4,200,1,3,2])


    int_nums = int(input("请输入"))







