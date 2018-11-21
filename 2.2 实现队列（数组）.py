# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 0021 上午 10:42
# @Author  : 杨宏兵
# @File    : 2.2 实现队列（数组）.py
# @Software: PyCharm
class MyQueue:
    def __init__(self):
        self.items = []
        self.front = 0
        self.rear = 0

    def enMyQueue(self,value):#队列添加元素
        self.items.append(value)
        self.rear += 1
        print('值%d添加队列成功！！！！'%value)
        return None

    def deMyQueue(self):#队列删除元素
        if self.front == self.rear:
            print("队列已经空了，没有办法删除元素！！！")
            return None
        self.items.pop()
        self.rear -= 1
        return None

    def isEmpty(self):#判断队列是非为空
        if self.front == self.end:
            print(" 队列是空的！！！")
            return None
        else:
            print('队列不是空的！！！')
            return None

    def size(self):#判读队列的长度
        return len(self.items)

    def getBack(self):#得到队列末尾的元素
        if self.rear > self.front:
            return self.items[len(self.items)-1]
        print('队列已经空了！')
        return None