# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 0019 下午 5:04
# @Author  : 杨宏兵
# @File    : 合并两个有序链表.py
# @Software: PyCharm


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def construck(link_length, distance):
    head = LNode()
    head.data = 'head'
    head.next = None
    i = 0
    cur = head
    while i < link_length:
        newNode = LNode()
        newNode.data = i + distance
        cur.next = newNode
        cur = cur.next
        i += 1
    return head

link1 = construck(6,0)















