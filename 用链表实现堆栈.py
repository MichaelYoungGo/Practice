# _*_ coding: utf-8 _*_


class Node:
    def __init__(self):
        self.data = 0
        self.next = 0


top = 0

def isEmpty():
    global top
    if (top == None):
        return 1
    else:
        return 0


def push(data):
    global top
    new_add_node = Node()
    new_add_node.data = data
    new_add_node.next = top
    top = new_add_node


def pop():
    global top
    if isEmpty():
        print('======当前堆栈为空=============')
        return -1
    else:
        ptr = top
        top = top.next
        temp = ptr.data
        return temp



while True:
    i = int(input('要压入堆栈，请输入1，要弹出则输入0， 停止操作则输入-1：'))
    if i == -1:
        break
    elif i == 1:
        value = int(input('请输入元素值：'))
        push(value)
    elif i == 0:
        print('弹出的元素为%d' %pop())