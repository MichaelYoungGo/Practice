# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 0015 下午 5:28
# @Author  : 杨宏兵
# @File    : 利用堆栈找出排名前500.py
# @Software: PyCharm


import heapq
def getTop(data):
    rowSize = len(data)
    columnSize = len(data[0])
    result3 = [None]*columnSize
    heap = []
    i = 0
    while i < rowSize:
        arr = (None, None, None)
        arr = (-data[i][0], i, 0)
        heapq.heappush(heap, arr)
        i += 1
    num = 0
    while num < columnSize:
        d = heapq.heappop(heap)
        result3[num] = -d[0]
        num += 1
        if num >= columnSize:
            break
        arr = (-data[d[1]][d[2]+1], d[1], d[2]+1)
        heapq.heappush(heap, arr)
    return result3

data = [[29, 17, 14, 2, 1], [19, 17, 16, 15, 6], [30, 25, 20, 14, 5]]
print(getTop(data))