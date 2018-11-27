# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 0027 下午 4:14
# @Author  : 杨宏兵
# @File    : 4.1 找出数组中的N重复元素.py
# @Software: PyCharm
def findDup(arrey, num):
    s = set()
    if None == arrey:
        return s
    lens = len(arrey)
    index = arrey[0]
    num = num - 1
    while True:
        if arrey[index] < 0:
            num -= 1
            arrey[index] = lens - num
            s.add(index)
        if num == 0:
            return  s
        arrey[index] *= -1
        index = arrey[index]*(-1)
if __name__=='__main__':
    arrey = [6, 2, 3, 3, 3, 4, 5, 5, 4, 5, 1]
    num = 6
    s = findDup(arrey, 6)
    for i in s:
        print(i)