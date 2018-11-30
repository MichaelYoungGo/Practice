# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 0030 下午 2:47
# @Author  : 杨宏兵
# @File    : 4.12 数组旋转45度.py
# @Software: PyCharm
def rotateArr(arr):
    lens = len(arr)
    i = lens - 1
    while i > 0:
        row = 0
        col = i
        while col < lens:
            print(arr[row][col])
            row += 1
            col += 1
        print('\n')
        i -= 1
    i = 0
    while i < lens:
        row = i
        col = 0
        while row < lens:
            print(arr[row][col])
            row += 1
            col += 1
        print('\n')
        i += 1

if __name__=="__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotateArr(arr)