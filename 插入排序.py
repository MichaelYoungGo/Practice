# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 0014 下午 5:07
# @Author  : 杨宏兵
# @File    : 插入排序.py
# @Software: PyCharm

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return  lists

lists = [38, 65, 97, 76, 13, 27, 49]
insert_sort(lists)
print(lists)