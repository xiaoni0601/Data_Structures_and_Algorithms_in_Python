##十进制转二进制：Decimal notation To Binary number：
from pythonds.basic.stack import Stack
def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString
print(divideBy2(42))


####十进制转16进制以下任意进制：
from pythonds.basic.stack import Stack
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    baseString = ""
    while not remstack.isEmpty():
        baseString = baseString + digits[remstack.pop()]
    return baseString
print(baseConverter(42,2))
print(baseConverter(25,2))
print(baseConverter(25,16))