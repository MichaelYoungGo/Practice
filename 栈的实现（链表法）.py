# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 0021 上午 9:24
# @Author  : 杨宏兵
# @File    : 栈的实现（链表法）.py
# @Software: PyCharm
class LNode:  #节点类
    def __init__(self):
        self.data = None
        self.next = None


class Stack:#栈类
    def __init__(self):
        self.data = 'head'
        self.next = None
    def isEmpty(self):
        if self.next == None:
            print('栈已经空了')
            return
        else:
            return False
    def size(self):
        size = 0
        if self.next != None:
            size +=1
            self.next == self.next.next
        return size
    def push(self,value):
        newNode = LNode()
        newNode.data = value
        self.next = newNode
        newNode.next = self.next
        print('压栈成功+%d+!!!!!' %newNode.data)
        return None
    def pop(self):
        ptr = self.next
        if ptr != None:
            print('弹栈成功%d'%self.next.data)
            self.next = self.next.next
            return None
        else:
            print('栈已经空了，无法进行弹栈操作！')
            return None
    def top(self):
        print(self.next.data)


newStack = Stack()
newStack.push(2)
newStack.push(3)
newStack.push(5)
newStack.top()
newStack.size()
newStack.pop()