# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 0023 下午 5:51
# @Author  : 杨宏兵
# @File    : test.py
# @Software: PyCharm
import math
number = 8
lens = int(math.log(8)/math.log(2))
print(lens)
number -= 1 << lens
print(number)
