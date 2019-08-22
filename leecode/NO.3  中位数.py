# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 18:32
# @Author  : 杨宏兵
# @File    : NO.3  中位数.py
# @Software: PyCharm
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        length1, length2 = len(nums1), len(nums2)
        i, j = 0, 0
        nums = []
        while i < length1 and j < length2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i = i + 1
                continue
            if nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j = j + 1
                continue
        if i < length1:
            nums.extend(nums1[i:length1])
        if j < length2:
            nums.extend(nums2[j:length2])
        length = length1 + length2
        index = length // 2
        if length%2 == 0:
            median = float((nums[index]+nums[index-1]))/2
        else:
            median = nums[index]
        return median

if __name__ == "__main__":
    solution = Solution()
    result = solution.findMedianSortedArrays([], [3, 4])
    print(result)





