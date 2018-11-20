# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 0016 下午 4:33
# @Author  : 杨宏兵
# @File    : 链表的逆转（就地实现）.py
# @Software: PyCharm
class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def Reverse(head):
    if head==None or head.next == None:
        return
    pre = None
    cur = head
    while cur:
        head = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return head


i = 1
head = LNode()
head.data = 'head'
head.next = None
ptr = head
while i<7:
    tmp = LNode()
    tmp.data = i
    ptr.next = tmp
    ptr = tmp
    i += 1
ptr = head.next
print('链表反转之前')
while ptr:
    print(ptr.data)
    ptr = ptr.next
print('链表反转之后')
ptr = Reverse(head)
while ptr:
    print(ptr.data)
    ptr = ptr.next



































