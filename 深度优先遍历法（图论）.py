# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 0008 下午 4:08
# @Author  : 杨宏兵
# @File    : 深度优先遍历法（图论）.py
# @Software: PyCharm


class list_node:
    def __init__(self):
        self.val = 0
        self.next = None


head = [list_node()]*9
run = [0]*9

data = [[1, 2], [2, 1], [1, 3], [3, 1],\
        [2, 4], [4, 2], [2, 5], [5, 2],\
        [3, 6], [6, 3], [3, 7], [7, 3],\
        [4, 8], [8, 4], [5, 8], [8, 5],\
        [6, 8], [8, 6], [8, 7], [7, 8]]

for i in range(1, 9):
    run[i] = 0
    head[i] = list_node()
    head[i].val = i
    head[i].next = None
    ptr = head[i]
    for j in range(20):
        if data[j][0] == i:
