# 递归Recursion：
# 1.将问题分解为规模更小的相同问题；
# 2.持续分解，直到可以用非常简单直接的方式来解决；
# 3.调用自身

#递归三定律：
# 1.必须有一个基本结束条件（最小规模）；
# 2.必须能改变状态向基本结束条件演进（减小问题规模）；
# 3.必须调用自身（解决减小来规模的相同问题）


# 应用例子1: 数列求和：
# 正常思路：通过迭代循环与累加变量，来做迭代求和
def listsum(numlist):
    theSum = 0         #累加变量theSum
    for i in numlist:  #for迭代循环
        theSum = theSum + i
    return theSum
print(listsum([1,3,5,7,9]))
# -----------------------------------------------------------------------------------------
# 假设没有循环语句：
# 递归思路：将规模大的列表求和-->分解为规模小的2个数求和:
# [1,3,5,7,9]-->全括号表达式：(1+(3+(5+(7+9))))-->(1+(3+(5+16)))-->(1+(3+21)))-->(1+24)-->25
def listsum(numlist):
    #最小规模，基本结束条件，只有一个值，求和就是返回本身
    if len(numlist) == 1:
        return numlist[0]
    #（减小规模：第一个数+余下的数）+ (余下的数，调用自身（listsum()）)：
    else:
        return numlist[0] + listsum(numlist[1:])  #调用自身函数listsum
print(listsum([1,3,5,7,9]))   

##递归应用：整数转换为任意进制
# 用最熟悉的十进制为例进行分析问题：
#   基本结束条件：小于10的整数
#   整数除，求余数往基本结束条件演进；
#   余数（% base）总是小于进制基，是基本结束条件；
#   整数商（// base）成为更小规模，通过调用自身递归

def toStr(n,base):
    convertString = '0123456789ABCDEF'  
    if n < base: #基本结束条件
        return convertString[n]
    else:
        #（减小n的规模:n // base） + （调用自身:toStr()）
        return toStr(n // base, base) + convertString[n%base]
print(toStr(1433,8))
print(toStr(1433,16))
print(toStr(1433,2))




