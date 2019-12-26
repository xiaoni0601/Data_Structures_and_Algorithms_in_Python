##通用的中缀转前缀算法:
from pythonds.basic.stack import Stack
def infixToPrefix(infixexpr):
    ##记录操作符的优先级
    prec = {}
    
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    prefixList = []
    tokenList = reversed(infixexpr.split())###：反转，来实现从右到左的扫描

    for token in tokenList:

        ##如果扫描是操作数，将其附加输出到列表末尾
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        
        ##如果是右括号，将其压倒opStack上
        elif token == ')':
            opStack.push(token)
        
        ##如果标记是左括号，则弹出 s，直到删除相应的右括号。将每个运算符附加到输出列表的末尾
        elif token == '(':
            while opStack.seek() != ')':
                prefixList.append(opStack.pop())
            opStack.pop()
        
        # 如果标记是运算符， *，/，+  或  -  ，将其压入 s。
        # 但是，首先删除已经在s中具有更高或相等优先级的任何运算符，并将它们加到输出列表中
        else:
            while (not opStack.isEmpty()) and \
                (opStack.peek() != ')') and \
                (prec[opStack.peek()] > prec[token]):
                prefixList.append(opStack.pop())               
            opStack.push(token)
    # 当输入表达式被完全处理时，检查 s。
    # 仍然在栈上的任何运算符都可以删除并加到输出列表的末尾
    while not opStack.isEmpty():
        prefixList.append(opStack.pop())
    
    #反转序列
    prefixList.reverse()
    return "".join(prefixList)

print(infixToPrefix("A + B * C"))