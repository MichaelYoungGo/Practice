# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 22:46
# @Author  : 杨宏兵
# @File    : No.5 Manacher Algorithm.py
# @Software: PyCharm


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_ = "#" + "#".join(s) + "#"
        lens = len(s_)
        mx = 0
        p = [0]*lens
        id = 0
        for i in range(0, lens):
            if i < mx:
                p[i] = min(mx-i, p[2*id-i])
            else:
                p[i] = 1
            while i - p[i] >= 0 and i + p[i] < lens and s_[i - p[i]] == s_[i + p[i]]:  # 满足回文条件的情况下
                p[i] += 1  # 两边扩展
            if (i + p[i]) > mx:  # 新子串右边界超过了之前最长子串右边界
                mx, id = i + p[i], i
        i_res = p.index(max(p))  # 获取最终最长子串中心位置
        s_res = s_[i_res - (p[i_res] - 1):i_res + p[i_res]]  # 获取最终最长子串，带"#"
        return s_res.replace('#', '')

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('cbbd'))
