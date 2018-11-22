# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 0021 下午 3:41
# @Author  : 杨宏兵
# @File    : 2.3 翻转栈的所有元素.py
# @Software: PyCharm
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print("压栈成功！%d"%value)

    def pop(self):
        if len(self.items) != 0:
            print("弹栈成功！%d" % self.items[len(self.items)-1])
            return self.items.pop()
        else:
            print('栈已经为空，无法进行出栈操作！！！')

    def top(self):
        if len(self.items) != 0:
            return self.items[len(self.items)-1]
        else:
            print('栈已经为空，栈顶没有元素！！！')

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False


def movebottonmtotop(sta):
    if sta.isEmpty():
        print("空栈，无法进行翻转")
        return None
    top1 = sta.top()
    sta.pop()
    if not sta.isEmpty():
        movebottonmtotop(sta)
        top2 = sta.top()
        sta.pop()
        sta.push(top1)
        sta.push(top2)
    else:
        sta.push(top1)


def revers(sta):
    if sta.isEmpty():
        return
    movebottonmtotop(sta)
    top = sta.top()
    sta.pop()
    revers(sta)
    sta.push(top)





if __name__ == '__main__':
    newStack = Stack()
    i = 0
    while i <4:
        newStack.push(i+1)
        i += 1
    print('栈进行翻转之前：')
    revers(newStack)
    print('栈进行翻转之后：')
    while not newStack.isEmpty():
        print(newStack.top())
        newStack.pop()

