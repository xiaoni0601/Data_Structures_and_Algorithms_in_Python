# 贪心策略
# 找零兑换问题,不同面值因硬币组合得到的最小个数的硬币结果：
# 递归解法：
# 以下解法，过于重复计算，效率极低

def recMC(coinValuelist,change):
    minCoins = change
    if change in coinValuelist:
        return 1
    else:
        for i in [c for c in coinValuelist if c <= change]:
            numCoins = 1 + recMC(coinValuelist,change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

import time
print(time.clock())
print(recMC([1,5,10,25],63))
print(time.clock())


#递归解法之改进：


def recDC(coinValuelist,change,knownResults):
    minCoins = change
    if change in coinValuelist:  # 递归基本结束条件
        knownResults[change] = 1 # 记录最优解
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]  # 查表成功，直接用最优解
    else:
        for i in [c for c in coinValuelist if c <= change]:
            numCoins = 1 + recDC(coinValuelist, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                
                knownResults[change] = minCoins #找到最优解，记录到表中
    return minCoins

print(recDC([1,5,10,25],63,[0]*64))
import time
print(time.clock())
print(recDC([1,5,10,25],63,[0]*64))
print(time.clock())


