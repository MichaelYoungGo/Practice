# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 0030 下午 3:59
# @Author  : 杨宏兵
# @File    : 4.14 集合的所有子集.py
# @Software: PyCharm
def getAllSubset(str):
    if str == None or len(str) < 1:
        print('参数不合理')
        return None
    arr = []
    arr.append(str[0:1])
    i = 1
    while i < len(str):
        lens = len(arr)
        j = 0
        while j < lens:
            arr.append(arr[j]+str[i])
            j += 1
        arr.append(str[i:i+1])
        i += 1
    return arr
if __name__=='__main__':
    result = getAllSubset('abc')
    i = 0
    while i <len(result):
        print(result[i])
        i += 1