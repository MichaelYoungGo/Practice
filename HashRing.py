# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 23:05
# @Author  : 杨宏兵
# @File    : HashRing.py
# @Software: PyCharm
import hashlib

content = """In computer science, consistent hashing is a special kind of 
hashing such that when a hash table is resized, only K/n keys need to be 
remapped on average, where K is the number of keys, and n is the number of 
slots. In contrast, in most traditional hash tables, a change in the number 
of array slots causes nearly all keys to be remapped because the mapping 
between the keys and the slots is defined by a modular operation."""

servers = [
    "10.10.1.1",
    "10.10.2.2",
    "10.10.3.3",
    "10.10.4.4",
]


class HashRing(object):
    """
     构造哈希环
    """

    def __init__(self, nodes=None, replicas=100):
        self.replicas = replicas
        self.ring = {}
        self._sort_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        """
        向哈希环中添加节点
        :param node:
        :return:
        """
        for i in range(0, self.replicas):
            key = self.gen_key("%s#%s" % (node, i))
            self.ring[key] = node
            self._sort_keys.append(key)
        self._sort_keys.sort()

    def get_node(self, string_key):
        """
        根据string_key的选择合适nodes
        :param string_key:
        :return:
        """
        return self.get_node_pos(string_key)[0]

    def get_node_pos(self, string_key):
        """
        在所有的节点中，nodes和虚拟nodes中寻找合适的位置。
        此处可以大作文章，所有节点构成的数据结构直接影响Hashing的性能，可以使用很多算法来优化
        例如： 链表， 数组，二叉树，B-树， 红黑树等
       :param string_key:
        :return:
        """
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)
        nodes = self._sort_keys
        for i in range(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                return self.ring[node], i
        return self.ring[nodes[0]], 0

    def remove_node(self, node):
        """
        删除节点和虚拟节点
        :param node:
        """
        for i in range(0, self.replicas):
            key = self.gen_key("%s#%s" % (node, i))
            del self.ring[key]
            self._sort_keys.remove(key)

    def gen_key(self, key):
        m = hashlib.md5()
        m.update(key.encode("utf8"))
        ret = m.hexdigest()
        return ret


def load_balance():
    """
    模拟服务器负载平衡
    :return:
    """

    hashring = HashRing(servers)
    words = content.split()

    database = {s: [] for s in servers}

    for idx in range(len(words)):
        node = hashring.get_node(words[idx])
        database[node].append(words[idx])
    for key, value in database.items():
        print("Server-%s:" % key, value)
    return database


if __name__ == "__main__":
    result = load_balance()
