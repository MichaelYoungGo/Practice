# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 0007 下午 12:46
# @Author  : 杨宏兵
# @File    : 5.10 求字符串中的最长回文子串.py
# @Software: PyCharm


class Test(object):
    def __init__(self):
        self.startIndex = None
        self.lens = None

    def getStartIndex(self):
        return self.startIndex

    def getLen(self):
        return self.lens

    def getLongestPalindrome(self, strs):
        if strs is None:
            return
        n = len(strs)
        if n < 1:
            return
        self.startIndex = 0
        self.lens = 1
        historyRecord = [([None] * n) for i in range(n)]
        i = 0
        while i < n:
            j = 0
            while j < n:
                historyRecord[i][j] = 0
                j += 1
            i += 1
        i = 0
        while i < n:
            historyRecord[i][i] = 1
            i += 1
        i = 0
        while i < n - 1:
            if list(strs)[i] == list(strs)[i + 1]:
                historyRecord[i][i + 1] = 1
                self.startIndex = i
                self.lens = 2
            i += 2
        pLen = 3
        while pLen <= n:
            i = 0
            while i < n - pLen + 1:
                j = i + pLen - 1
                if list(strs)[i] == list(strs) and (historyRecord[i + 1][j - 1] == 1):
                    historyRecord[i][j] == 1
                    self.startIndex = i
                    self.lens = pLen
            pLen += 1


if __name__ == "__main__":
    strs = "abcdefgfedxyz"
    t = Test()
