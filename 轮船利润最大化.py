import random

listOne = []
for i in range(26):
    temp = random.randint(10, 100)
    listOne.append(temp)

# 测试数据 26个港口的价格
print("港口价格:", listOne)


def maxProfit(tempList):
    # 计算轮船的最大收益

    newList = []
    for i in range(len(tempList)):
        if i < len(listOne) - 1:
            # 后港口-前港口
            chazhi = tempList[i + 1] - tempList[i]
            newList.append(chazhi)


    # 港口增值数
    newList2 = []
    print('轮船买卖货物的方案：')
    for i in newList:
        # 将增值保存到列表
        if i > 0:
            print('%d号港口买入，%d号港口卖出' % (newList.index(i), newList.index(i)+1))
            newList2.append(i)

    return sum(newList2)


if __name__ == '__main__':
    result = maxProfit(listOne)
    print("港口最大收益：", result)




