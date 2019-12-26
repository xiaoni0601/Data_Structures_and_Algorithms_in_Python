#后缀表达式求值：
from pythonds.basic.stack import Stack
def postfixEval(postfixExpr):
    #定义空栈，用于暂存操作数
    operandStack = Stack()
    #将后缀表达式split()解析得到token列表
    tokenList = postfixExpr.split()
    
    for token in tokenList:##从左到右扫描，不断进行for循环：
        
        ##如果是操作数,将token转换成int整数，压入operandStack栈顶：
        if token in "0123456789":
            operandStack.push(int(token))
        
        ##如果遇见的是操作符，求值开始。
        # 从栈顶弹出2个操作数，删除操作数：
        else:
            op2 = operandStack.pop()#先pop出来的是2
            op1 = operandStack.pop()#接着pop出来的是1
            result = doMath(token,op1,op2)#：进行该操作符运算
            operandStack.push(result)#：将运算结果重新push压入栈顶
    ##返回弹出的栈顶值
    return operandStack.pop()

def doMath(op,op1,op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval("4 5 6 * +"))
#>>> 4 + 5*6
#34
print(postfixEval("4 5 6 * -"))
#>>> 4 - 5*6
#-26
print(postfixEval("4 5 6 / +"))
#>>> 4 + 5/6
#4.833333333333333
print(postfixEval("4 5 6 / -"))
#>>> 4 - 5/6
#3.1666666666666665
