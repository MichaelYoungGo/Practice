# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 0008 下午 2:33
# @Author  : 杨宏兵
# @File    : 无向图邻接矩阵.py
# @Software: PyCharm



arr = [[0]*6 for row in range(6)]
print(arr)

data = [[1, 2], [2, 1], [1, 5], [5, 1],\
        [2, 3], [3, 2], [2, 4], [4, 2],\
        [3, 4], [4, 3]]
print(data)

for i in range(10):
    for j in range(2):
        for k in range(6):
            tmpi = data[i][0]
            tmpj = data[i][1]
            arr[tmpi][tmpj] = 1

print('无向图矩阵')
for i in range(1,6):
    for j in range(1,6):
        print('[%d]' %arr[i][j], end=' ')
    print()
