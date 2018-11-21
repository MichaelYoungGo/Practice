# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 0021 上午 9:04
# @Author  : 杨宏兵
# @File    : 实现栈（数组实现）.py
# @Software: PyCharm
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # 返回栈顶大小
    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    #弹栈
    def pop(self):
        if len(self.items)>0:
            self.items.pop()
        else:
            print("栈已经为空")
            return None
    #入栈
    def push(self,item):
        self.items.append(item)


s = Stack()
s.push(5)
s.pop()