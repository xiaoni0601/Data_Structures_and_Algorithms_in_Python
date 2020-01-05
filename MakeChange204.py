# 动态规划算法de扩展：
# 列出最少硬币数的组合

def dpMakeChange(coinValuelist, change, minCoins, coinsUsed):
    # 从1分开始到change逐个计算最小硬币数
    for cents in range(1, change + 1):   # ()表示左闭右开，因此change+1 
        # 1.初始化一个最大值
        coinCount = cents
        # 将新加硬币进行初始化
        newCoin = 1
        # 2. 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValuelist if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j # 对应最小数量，所减的硬币
        # 3. 得到当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    # 返回最后1个结果
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

amnt = 63
clist = [1, 5, 10, 21, 25]
coinsUsed = [0] * (amnt + 1)
coinCount = [0] * (amnt + 1)

print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
printCoins(coinsUsed, amnt)
print(coinsUsed)

