# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 0026 下午 4:45
# @Author  : 杨宏兵
# @File    : 4.1 找出数组中唯一的重复元素（空间换时间法））.py
# @Software: PyCharm
def findDup(arrey):
    if None == arrey:
        return -1
    lens = len(arrey)
    hashTable = dict()
    i =0
    while i < lens - 1:
        hashTable[i] = 0
        i += 1
    j = 0
    while j < lens:
        if hashTable[arrey[j]-1] == 0:
            hashTable[arrey[j] - 1] = arrey[j]
        else:
            return arrey[j]
        j += 1
    return -1


if __name__=='__main__':
    arrey = [1, 3, 4, 2, 1, 5]
    print(findDup(arrey))






