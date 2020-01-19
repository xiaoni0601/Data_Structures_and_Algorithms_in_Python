# 建立表达式解析树的思路：
# 关键点：对当前节点的跟踪
# 创建左右子树：调用insertLeft/insertRight
# 设置当前节点值：调用 setRootVal
# 下降到左右子树：调用getLeftChild/RightChild
# 下降前的节点：push入栈
# 上升前的节点：pop出栈

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree) # --入栈下降
    currentTree = eTree
    for i in fplist:   
        if i == '(':  # 表达式开始：
            currentTree.insertLeft('')
            pStack.push(currentTree) # --入栈下降
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']: # --操作数
            currentTree.setRootVal(int(i))
            parent = pStack.pop()   # --出栈上升
            currentTree = parent
        elif i in ['+', '-', '*', '/']:  # --操作符
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':  # --表达式结束
            currentTree = pStack.pop() # --出栈上升
        else:  # --防止出错，意外处理
            raise ValueError
    return eTree


# 利用表达式解析树求值：
import operator
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, \
        '*':operator.mul, '/':operator.truediv}  # --字典dic()映射
        leftC = parseTree.getLeftChild()
        rightC = parseTree.getRightChild()

        if leftC and rightC:
            fn = opers[parseTree.getRootVal()]
            return fn(evaluate(leftC), evaluate(rightC))
        else:
            return parseTree.getRootVal()


# 利用后序遍历进行表达式求值（左子树-->右子树-->根的顺序）：
def postorderval(tree):
    opers = {'+':operator.add, '-':operator.sub, \
        '*':operator.mul, '/':operator.truediv}  # --字典dic()映射
    res1 = None
    res2 = None
    if tree:
        res1 = postorderval(tree.getLeftChild())  # --计算左子树的值
        res2 = postorderval(tree.getRightChild())  # --计算右子树的值
        if res1 and res2:
            return opersp[tree.getRootVal()](res1, res2)  # 左右子树的值进行根运算符计算
        else:
            return tree.getRootVal()



# 利用中序遍历进行生成全括号中缀表达式：
def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal