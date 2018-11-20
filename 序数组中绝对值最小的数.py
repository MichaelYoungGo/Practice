def getMinabc(alist):
    '''n=1，没有商量的余地，直接返回
      a[0] * a[n-1] >= 0，说明这些元素同为非正或同为非负。
      要是a[0]>=0，返回a[0]；否则返回a[n-1]
      a[0] * a[n-1] < 0，说明这些元素中既有整数，也有负数。此时需要计算中间位置为mid = low + high/2，
      如果a[mid]*a[low] >=0说明a[mid]也为非正，缩小范围low=mid；
      如果a[mid]*a[high]>=0，说明a[mid]非负，缩小范围high=mid。
      在期间如果还有两个元素，那么就比较以下他俩，直接返回了'''
    length = len(alist)
    low = 0
    high = length-1
    if length == 1:
        return alist[0]
    if alist[0] >= 0:
        return alist[0]
    if alist[length-1] <= 0:
        return alist[length-1]
    while low < high:
        mid = (low + high)// 2
        if low+1 == high:
            if abs(low) < abs(high):
                return alist[low]
            else:
                return alist[high]
        if alist[low]*alist[mid] >= 0:
            low = mid
        if alist[high]*alist[mid] >= 0:
            high = mid


a = [-2, -1, 3, 4, 5]
result = getMinabc(a)
print(result)m