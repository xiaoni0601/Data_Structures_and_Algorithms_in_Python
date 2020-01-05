# 每日温度（10分）
# 根据每日气温列表，请重新生成一个列表，
# 对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。
# 如果之后都不会升高，请在该位置用 0 来代替
def dailyTemperatures(T):
    stack = []
    res = [0] * len(T)
    for i in range(len(T) - 1, -1, -1):
        t = T[i]
        while stack and stack[-1][1] <= t:
            stack.pop()
        if stack:
            res[i] = stack[-1][0] - i
        stack.append((i, t))
    return res
print(dailyTemperatures([73,74,75,71,69,72,76,73]))