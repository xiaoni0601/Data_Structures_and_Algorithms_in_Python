# 二叉查找树
# 二叉查找树的性质：
# 比父节点小的key都出现在左子树，比父节点大的key都出现在右子树

# 二叉查找树：BST.delete
# _get() 找到--> remove()删除
def delete(self, key):
    
    # size > 1:
    if self.size > 1:
        nodeToRemove = self._get(key, self.root)  # --通过_get()找到
        if nodeToRemove:   # --找得到
            self.remove(nodeToRemove)
            self.size = self.size - 1
        else:  # -- get()找不到
            raise KeyError('Error, key not in tree')
    
    # size == 1:
    elif self.size == 1 and self.root.key == key:
        self.root = None
        self.size = self.size - 1
    else:
        raise KeyError('Error, key not in tree')

def __delitem__(self, key):
    self.delete(key)


# 二叉查找树：BST.remove():
# remove的这个节点分3种情形：1. 是个叶节点，没有子节点；2.有一个子节点； 3.有两个子节点

# 1. 是叶节点情形，直接删除：
if currentNode.isLeaf():
    if currentNode == currentNode.parent.leftChild:
        currentNode.parent.leftChild = None
    else:
        currentNode.parent.rightChild = None


# 2. 一个子节点， 将唯一的这个子节点上移，替换掉被删节点的位置：
# 替换操作继续分情形：
# 1.被删节点的子节点是左子节点，还是右子节点？ 
# 2. 被删节点本身是父节点的左子节点还是右子节点？ 
# 3. 被删节点本身是根节点？
else: ## this node has one child
    if currentNode.hasLeftChild():
        if currentNode.isLeftChild():
            # 左子节点删除：
            currentNode.leftChild.parent = currentNode.parent
            currentNode.parent.leftChild = currentNode.leftChild
        elif currentNode.isRightChild():
            # 右子节点删除：
            currentNode.leftChild.parent = currentNode.parent
            currentNode.parent.rightChild = currentNode.leftChild
        else:
            # 根节点删除：
            currentNode.replaceNodeData(currentNode.leftChild.key,
                               currentNode.leftChild.payload,
                               currentNode.leftChild.leftChild,
                               currentNode.leftChild.rightChild) 
    else:
        if currentNode.isLeftChild():
            # 左子节点删除
            currentNode.rightChild.parent = currentNode.parent
            currentNode.parent.leftChild = currentNode.rightChild
        
        elif currentNode.isRightChild():
            # 右子节点删除
            currentNode.rightChild.parent = currentNode.parent
            currentNode.parent.rightChild = currentNode.rightChild
        else:
            # 根节点删除
            currentNode.replaceNodeData(currentNode.rightChild.key,
                               currentNode.rightChild.payload,
                               currentNode.rightChild.leftChild,
                               currentNode.rightChild.rightChild)



# 3.被删节点有2个子节点：找到另外一个合适的节点“后继”successor，来替换被删节点
elif currentNode.hasBothChildren():
    succ = currentNode.findSuccessor() # --找到后继findSuccessor,赋值给succ
    succ.spliceOut()   # --将succ摘出
    currentNode.key = succ.key  # -- succ的key替换掉currentNode的key
    currentNode.payload = succ.payload     # --succ的payload 替换掉currentNode的payload

def findSuccessor(self): # --寻找后继
    succ = None
    if self.hasRightChild():  # --当前节点如果有右节点
        succ = self.rightChild.findMin()   # --右子节点中的最小findMin就是赋值给succ
    else:
        if self.parent:
            if self.isLeftChild():
                succ = self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
    return succ

def findMin(self):
    current = self
    while current.hasLeftChild(): # --左的永远小于右的，只需要找左下角返回即可
        current = current.leftChild
    return current    


# 摘出节点spliceOut()
def spliceOut(self):
    if self.isLeaf(): # --叶节点，直接摘出
        if self.isLeftChild():
            self.parent.leftChild = None
        else:
            self.parent.rightChild = None
    elif self.hasAnyChilidren():
        if self.hasLeftChild():
            if self.isLeftChild():
                self.parent.leftChild = self.leftChild
            else:
                self.parent.rightChild = self.leftChild
            self.leftChild.parent = self.parent
        
        else: # 摘出带右子节点的节点：
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
            self.rightChild.parent = self.parent