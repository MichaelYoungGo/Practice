# _*_coding: utf-8_*_

import  sys
class empolyee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None


def findnode(head, num):
    ptr = head
    while ptr.next != head:
        if ptr.num == num:
            return ptr
        ptr = ptr.next
    return ptr


def insertnode(head, after, new_num, new_name, new_salary):
    InserNode = empolyee()
    CurNode = None
    InserNode.num = new_num
    InserNode.name = new_name
    InserNode.salary = new_salary
    if InserNode == None:
        print('内存分配失败')
        return None
    else:
        if after.next == head:
            InserNode.next = head
            CurNode ==head
            while CurNode.next != head:
                CurNode = CurNode.next
            CurNode.next = InserNode
            head = InserNode
            return head
        else:
            InserNode.next = after.next
            after.next = InserNode
            return head


position = 0
namedata = ['Allen', 'Scott', 'Marry', 'John', 'Mark', 'Rickly',
            'Lisa', 'Jisica', 'Hanson', 'Amy', 'Bob', 'Jack']
data = [[1001, 32368], [1002, 32368], [1003, 32368], [1007, 32368],
        [1012, 32368], [1014, 32368], [1018, 32368], [1043, 32368],
        [1031, 32368], [1037, 32368], [1041, 32368], [1046, 32368]]
print("员工编号 薪水 员工编号 薪水 员工编号 薪水 员工编号 薪水")
print('-------------------------------------------------------')
for i in range(3):
    for j in range(4):
        print('[%2d] [%3d]' %(data[i*4+j][0], data[i*4+j][1]), end='')
    print()

head = empolyee()
if not head:
    print('error! 内存分配失败！！！')
    sys.exit(0)

head.num = data[0][0]
head.name = namedata[0]
head.salary = data[0][1]
head.next = None
ptr = head
for i in range(1, 12):
    newnode = empolyee()
    newnode.num = data[i][0]
    newnode.name = namedata[i]
    newnode.salary = data[i][1]
    newnode.next = None
    ptr.next = newnode
    ptr = newnode

newnode.next = head

while True:
    print('请输入要插入其后的员工编号，如果输入的编号不在此链表中，')
    position = int(input('则新输入的员工节点将视为此'
                         '链表的第一个节点，要结束插入过程请输入-1：'))
    if position == -1:
        break
    else:
        ptr = findnode(head, position)
        new_num = int(input('请输入新员工编号：'))
        new_name = input('请输入新员工的名字：')
        new_salary = int(input('请输入新员工的薪水'))
        head = insertnode(head, ptr, new_num, new_name, new_salary)

ptr = head
print('\t员工编号\t姓名\t 薪水')
print('\t================================')

while True:
    print('\t[%2d]\t[%-10s]\t[%3d]' %(ptr.num, ptr.name, ptr.salary))
    ptr = ptr.next
    if head == ptr:
        break
