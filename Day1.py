# _*_ coding:utf-8 _*_
# Project Name: Python_Practice
# File Name: Day1
# Author： rockche
# Date:  2021/7/23  3:57 下午
# Description : Day1
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
n = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (k != i):
                print(i, j, k)
                n += 1
print(f"一共有{n}个数字")
