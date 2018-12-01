# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 0030 下午 5:43
# @Author  : 杨宏兵
# @File    : 4.19  构造新的数组.py
# @Software: PyCharm


def calculate(a,b):
    b[0] = 1
    N = len(a)
    i = 1
    while i < N:
        b[i] = b[i-1]*a[i-1]
        i += 1
    b[0] = a[N-1]
    i = N - 2
    while i >= 1:
        b[i] *= b[0]
        b[0] *= a[i]
        i -= 1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [None] * len(a)
    calculate(a, b)
    i = 0
    for i in b:
        print(i)