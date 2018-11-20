# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 0015 下午 1:27
# @Author  : 杨宏兵
# @File    : 堆排序.py
# @Software: PyCharm

def adjust_heap(lists, i, size):
    lchild = 2*i + 1
    rchild = 2*i + 2
    maxs = i
    if i < size/2:
        if lchild < size and lists[lchild] > lists[maxs]:
            maxs = lchild
        if rchild < size and lists[rchild] > lists[maxs]:
            maxs = rchild
        if maxs != i:
            lists[maxs], lists[i]=lists[i], lists[maxs]
            adjust_heap(lists, maxs, size)


def build_heap(lists, size):
    for i in range(0, int(size/2))[::-1]:
        adjust_heap(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists,size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


lists = [3, 4, 2, 8, 9, 5, 1]
heap_sort(lists)
print(lists)