# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 0021 下午 2:55
# @Author  : 杨宏兵
# @File    : 2.2队列实现（链表法）.py
# @Software: PyCharm
class LNode:
    def __init__(self):
        self.data = None
        self.next = None


class MyQueue:
    def __init__(self):
        self.data = 'head'
        self.pHead = None
        self.pEnd = None

    def size(self):  # 链表的长度
        if self.pHead == None:
            print("该队列是空队列！！！")
            return None
        else:
            i = 0
            while self.pHead != None:
                i += 1
                self.pHead = self.pHead.pHead
            print('队列的长度是%d' % i)
            return None

    def isEmpty(self):
        if self.pHead == None:
            print("该队列是空队列！！！")
            return None

    def enMyQueue(self, value):
        newNode = LNode()
        if self.pHead == None:
            self.pHead = self.pEnd = newNode
        else:
            self.pEnd.next = newNode
            self.pEnd = newNode
    def deQueue(self):
        if self.pHead != None:
            self.pHead = self.pHead.next
        else:
            print('队列已经空了，无法进行删除操作元素！！！！')








