
##通用的中缀转后缀算法:
from pythonds.basic.stack import Stack
def infixToPostfix(infixexpr):
    ##记录操作符的优先级
    prec = {}
    prec[")"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()#解析表达式到单词列表，从左到右扫描

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)

print(infixToPostfix("A+B*C"))
###infixexpr没有空格的output依然是本身：A+B*C
###infixexpr表达式要加空格才对了：
print(infixToPostfix("A + B * C"))