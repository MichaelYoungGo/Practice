# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 0001 上午 11:24
# @Author  : 杨宏兵
# @File    : 4.20 获取最好的矩阵链相乘方法.py
# @Software: PyCharm


def MatrixChainOrder(p, n):
    cost = [[None]*n for i in range(n)]
    i =1
    while i < n:
        cost[i][i] = 0
        i += 1
    cLen = 2
    while cLen < n:
        i = 1
        while i < n-cLen+1:
            j = i + cLen -1
            cost[i][j] = 2 ** 31
            k = i
            while k <= j - 1:
                q = cost[i][k] + cost[k+1][j] + p[i-1]*p[k]*p[j]
                if q < cost[i][j]:
                    cost[i][j] = q
                k += 1
            i += 1
        cLen += 1
    return cost[1][n-1]


if __name__ == '__main__':
    arr = [1, 5, 2, 4, 6]
    n = len(arr)
    result = MatrixChainOrder(arr, n)
    print(result)