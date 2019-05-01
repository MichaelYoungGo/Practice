#_*_ coding:utf-8 _*_
#归并排序


def splitlist(list):
    '''
    现有一个列表，里面元素包括 数字，字母，列表，字典等元素，现在要将字典去掉，并将列表
      分解成字母，或数字元素如：[[1,2,3],2,3,[1,3,[12,22]],'a',12]
      经函数处理后[1, 2, 3, 2, 3, 1, 3, 12, 22, 'a', 12]
    '''
    alist = []
    a = 0

    for sublist in list:
        try:  # 用try来判断是列表中的元素是不是可迭代的，可以迭代的继续迭代
            for i in sublist:
                alist.append(i)
        except TypeError:  # 不能迭代的就是直接取出放入alist
            alist.append(sublist)
    for i in alist:
        if type(i) == type([]):  # 判断是否还有列表
            a = + 1
            break
    if a == 1:
        return splitlist(alist)  # 还有列表，进行递归
    if a == 0:
        return alist


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    num = len(alist) // 2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    # 合并
    return merge(left, right)


def merge(left, right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    # left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    pass
    return result


alist = splitlist([[2, 4, 5], [1, 2, 3], [4, 5]])
sorted_alist = merge_sort(alist)
print(sorted_alist)

