# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 0001 下午 1:23
# @Author  : 杨宏兵
# @File    : 输入限制I的双向队列.py
# @Software: PyCharm

class Node:
    def __init__(self):
        self.data = 0
        self.next = None


front = Node()
rear = Node()
front = None
rear = None


def enquenue(value):
    global front
    global rear
    node = Node()
    node.data = value
    node.next = None
    if rear == None:
        front == node
    else:
        rear.next = node
    rear = node


def dequeue(action):
    global front
    global rear
    if (front != None) and action == 1:
        if front == rear:
            rear= None
        value = front.data
        front = front.next
        return value
    elif front != None and action ==2:
        startNode = front
        value = rear.data
        tempNode = front
        while front.next != rear and front != None:
            front = front.next
            tempNode = front
        front = startNode
        rear = tempNode
        if front.next == None or rear.next == None:
            front = None
            rear = None
        return value


    else:
        return -1


print('用链表来实现双向队列')
print('===============================================')

ch = 'a'
while True:
    ch = input('加入请按a, 取出请按d, 结束请按e')
    if ch == 'e':
        break
    elif ch == 'a':
        item = int(input('加入的元素值：'))
        enquenue(item)
    elif ch == 'd':
        temp = dequeue(1)
        print('从双向队列前端按序取出的元素值为：%d' %temp)
        temp = dequeue(2)
        print('从双向队列后端按序取出的元素值为：%d' % temp)
    else:
        break
