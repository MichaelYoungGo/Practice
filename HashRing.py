# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 23:23
# @Author  : 杨宏兵
# @File    : HashRing.py
# @Software: PyCharm


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


class NormalHash:
    def __init__(self, nodes=None):
        self.nodes = nodes if nodes else []
        self.count = len(nodes) if nodes else 0

    def get_node(self, value):
        if value < 0:
            return
        return self.nodes[value % self.count]


def load_balance():
    nh = NormalHash(servers)
    words = content.split()

    database = {s: [] for s in servers}

    for idx in range(len(words)):
        node = nh.get_node(idx)
        database[node].append(words[idx])

    print(database)


if __name__ == '__main__':
    load_balance()

