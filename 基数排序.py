# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 0015 下午 2:30
# @Author  : 杨宏兵
# @File    : 基数排序.py
# @Software: PyCharm
import math
def raix_sort(lists, radix = 10):
    k = int(math.ceil(math.log(max(lists),radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            print(int(j/(radix**(i-1)) % radix))
            bucket[int(j/(radix**(i-1)) % radix)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

lists = [3, 54, 118 ,9, 5, 1]
print(raix_sort(lists))


