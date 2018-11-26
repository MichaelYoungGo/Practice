# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 0025 下午 4:59
# @Author  : 杨宏兵
# @File    : 反向DNS查找缓存.py
# @Software: PyCharm


class TrieNode:
    def __init__(self):
        CHAR_COUNT = 11
        self.isLeaf = False
        self.url = None
        self.child = [None] * CHAR_COUNT
        i = 0
        while i < CHAR_COUNT:
            self.child[i] = None
            i += 1


def getIndexFromChar(c):
    return 10 if c == '.' else (ord(c) - ord('0'))


def getCharFromIndex(i):
    return '.' if i == 10 else ('0' + str(i))


class DNSCache():
    def __init__(self):
        self.CHAR_COUNT = 11
        self.root = TrieNode()

    def insert(self, ip, url):
        lens = len(ip)
        pCrawl = self.root
        level = 0
        while level < lens:
            index = getIndexFromChar(ip[level])
            if pCrawl.child[index] is None:
                pCrawl.child[index] = TrieNode()
            pCrawl = pCrawl.child[index]
            pCrawl.isLeaf = True
            pCrawl.url = url
            level += 1

    def searchDNSCache(self, ip):
        pCrawl = self.root
        lens = len(ip)
        level = 0
        while level < lens:
            index = getIndexFromChar(ip[level])
            if pCrawl.child[index] is None:
                return None
            pCrawl = pCrawl.child[index]
            level += 1
        if pCrawl != None and pCrawl.isLeaf:
            return pCrawl.url
        return None


ipAdds = ['10.57.11.127', '121.57.61.129', '66.125.100.103']
url = ['www.baidu.coom', 'www.google.com', 'www.sougou.com']
n = len(ipAdds)
cache = DNSCache()
for i in range(n):
    cache.insert(ipAdds[i], url[i])
    i += 1
ip = '121.57.61.129'
res_url = cache.searchDNSCache(ip)
if res_url != None:
     print(ip+'------>'+res_url)
else:
     print('没有这个IP')

