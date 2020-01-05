# 题目内容：
# ASCII谢尔宾斯基地毯（10分）

def carpet(N,C):
    def check(n,x,y):
        if n <= 1:
            return True
        n2 = n // 3 ##递归部分
        if n2 <= x < n2 * 2 and n2 <= y < n2 * 2:#中间挖空部分
            return False
        return check(n2, x%n2, y%n2)
    for y in range(N):
        for x in range(N):
            if check(N,x,y):
                print(C,end='')
            else:
                print(' '*len(C),end='')
        print('')
carpet(9,'*')
carpet(9,'[]')
carpet(10,'[]')