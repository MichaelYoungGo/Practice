# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 0022 下午 7:16
# @Author  : 杨宏兵
# @File    : 2.7 如何设计一排序系统.py
# @Software: PyCharm
from collections import deque


class User:  # 建立用户类
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def getNname(self):
        return self.name

    def setNname(self, name):
        self.name = name

    def getseq(self):
        return self.seq

    def setSeq(self, seq):
        self.seq = seq

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def toString(self):
        return 'id:'+str(self.id)+'   name:'+self.name+' seq:'+str(self.seq)


class MyQueue: #建立队列类
    def __init__(self):
        self.q = deque()

    def enQueue(self, user):
        user.setSeq(len(self.q)+1)
        self.q.append(user)

    def deQueue(self):
        self.q.popleft()
        self.update()

    def deQueuemove(self, user):
        self.q.remove(user)
        self.update()

    def update(self):
        i = 1
        for user in self.q:
            user.setSeq(i)
            i += 1

    def printMyQueue(self):
         for u in self.q:
             print(u.toString())


u1 = User(1, 'Admin')
u2 = User(2, 'Lucy')
u3 = User(3, 'Michael')
u4 = User(4, 'Robin')
queue = MyQueue()
queue.enQueue(u1)
queue.enQueue(u2)
queue.enQueue(u3)
queue.enQueue(u4)
queue.deQueue()
queue.deQueuemove(u3)
queue.printMyQueue()

