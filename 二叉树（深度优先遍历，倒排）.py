# -*- coding: utf-8 -*-
"""
Time: 2019-07-25 22:33
Author: MichaelYoung
"""
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


class Node(object):
    """
    构建二叉树的节点
    """
    def __init__(self, item=None, lchild=None, rchild=None):
        self.item = item
        self.left = lchild
        self.right = rchild


class BinaryTree(object):
    """"创建二叉树"""
    def __init__(self):
        self.root = Node()
        # 该队列用于存放正在操作的节点, 存放的顺序是根节点，左节点，右节点
        self.queue = []

    def add_node(self, number):
        new_node = Node(number)
        self.queue.append(new_node)
        if self.root.item is None:
            self.root.item = new_node
        else:
            tree_node = self.queue[0]
            if tree_node.left is None:
                tree_node.left = new_node
            else:
                tree_node.right = new_node
                self.queue.pop(0)
     

if __name__=="__main__":
    b_tree = BinaryTree()
    for i in xrange(0, 10):
        b_tree.add_node(i)
