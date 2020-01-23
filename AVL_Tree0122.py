# 平衡二叉查找树：AVL树：Adelson+Velskii+Landiss三人名字
# 平衡因子BalanceFactor：左右子树的高度差height(leftSbuTree) - height(rightSubTree)
# balanceFactor>0:left-heavy; balanceFactor<0:right-heavy; =0:balance

# N:总节点； h：树的高度 Nh=1 + Nh-1 + Nh-2

# AVL 插入新key-->进入叶节点-->沿路径传递-->1.直到根节点停止传递； or 2.某个父节点平衡因子被调整到0停止

# AVL树的实现：put()
def _put(self, key, val, currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key, val, currentNode.leftChild)
        else:
            currentNode.leftChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.leftChild)
    else:
        if currentNode.hasRightChild():
            self_put(key, val, currentNode.rightChild)
        else:
            currentNode.rightChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.rightChild)

# AVL树的实现：UpdateBalance()
def updateBalance(self, node):
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)  # --重新平衡
        return
    if node.parent != None:
        if node.isLeftChild():
            node.parent.balanceFactor += 1
        elif node.isRightChild():
            node.parent.balanceFactor -= 1
        if node.parent.balanceFactor != 0:
            self.updateBalance(node.parent)


# AVL树的实现：rebalance重新平衡：
# 将不平衡的子树进行旋转rotation + 更新父节点
# 左旋rotateLeft:
def rotateLeft(self, rotRoot):
    newRoot = rotRoot.rightChild
    rotRoot.rightChild = newRoot.leftChild
    if newRoot.leftChild != None:
        newRoot.leftChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    if rotRoot.isRoot():
        self.root = newRoot
    else:
        if rotRoot.isLeftChild():
            rotRoot.parent.rightChild = newRoot
        else:
            rotRoot.parent.rightChild = newRoot
    newRoot.leftChild = rotRoot
    rotRoot.parent = newRoot
    rotRoot.balanceFactor = rotRoot.balanceFactor + \
                            1 - min(newRoot.balanceFactor, 0)
    newRoot.balanceFactor = newRoot.balanceFactor + \
                            1 + max(rotRoot.balanceFactor, 0)     
    

# AVL树的实现：rebalance
def rebalance(self, node):
    if node.balanceFactor < 0: # --此时右重,需要进行左旋
        if node.rightChild.balanceFactor > 0:     
            # Do an LR Rotation,右子节点左重了，需要先右旋：
            self.rotateRight(node.rightChild)
            self.rotateLeft(node)
        else:
            # single left， 一个单纯的左旋即可
            self.rotateLeft(node)
    
    elif node.balanceFactor > 0: # --此时左重，需要右旋
        if node.leftChild.balanceFactor < 0:
            # Do an RL Rotation,左子节点右重了，先左旋
            self.rotateLeft(node.leftChild)
            self.rotateRight(node)
        else:
            # single right, 一个单纯的右旋即可
            self.rotateRight(node)