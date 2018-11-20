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


list = [[1, 2, 3], 2, 3, [1, 3, [12, 22, [2, 3]]], 'a', 12, range(10)]
a = splitlist(list)
print(a)
