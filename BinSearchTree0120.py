# 二叉查找树
# 二叉查找树的性质：
# 比父节点小的key都出现在左子树，比父节点大的key都出现在右子树

# 定义类 BST： BinarySearchTree:
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()

# 定义类 TreeNode:
class TreeNode:

    def __init__(self, key, val, left = None, \
        right = None, parent = None):
        self.key = key # --键
        self.payload = val  # --值
        self.leftChild = left # --左节点
        self.rightChild = right # --右节点
        self.parent = parent   # --父节点

    def hasLeftChild(self):
         return self.leftChild   
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and \
            self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and \
            self.parent.rightChild == self
    
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.hasLeftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    
    
# 二叉查找树： BST.put算法
# put(key, value):插入key，构造BST
def put(self, key, val):
    if self.root:
        self._put(key, val, self, root)  # --递归函数_put()
    else:
        self.root = TreeNode(key, val)
    self.size = self.size + 1

# _put(key, val, currentNode)辅助方法
def _put(self, key, val, currentNode):

    # 如果key比currentNode小：
    if key < currentNode.key:
        
        # 如果当前节点有左子树，_put()到左子树：
        if currentNode.hasLeftChild():
            self._put(key, val, currentNode.leftChild) 
        
        else: # 如果当前节点没有左子树，key就成为左子节点：
            currentNode.leftChild = \
                TreeNode(key, val, parent=currentNode)

    # 如果key比currentNode大：
    if key > currentNode:
        
        # 如果当前节点有右子树，_put()到右子树：
        if currentNode.hasRightChild():
            self._put(key, val, currentNode.rightChild)
        
        else: # 如果当前节点没有右子树，key就成为右子节点：
            currentNode.rightChild = \
                TreeNode(key, val, parent=currentNode)

# 二叉搜索树：索引赋值
def __setitem__(self, k, v):
    self.put(k, v)

# 二叉搜索树：BST.get():
# 在树中找到key所在节点对应的payload数据项
def get(self, key):
    if self.root:
        res = self._get(key, self.root)
        if res:
            return res.payload
        else:
            return None
    else:
        return None

def _get(self, key, currentNode):
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return self._get(key, currentNode.leftChild)
    else:
        return self._get(key, currentNode.rightChild)


# 二叉搜索树：索引和归属判断
def __getitem__(self, key):
    return self.get(key)

def __contains__(self, key):
    if self._get(key, self.root):
        return True
    else:
        return False

mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"
print(3 in mytree)
print(mytree[6])


# 二叉搜索树：迭代器
# 中序遍历的顺序，进行迭代
def __iter__(self):
    if self:
        if self.hasLeftChild():
            for elem in self.leftChild:
                yield elem # --每次迭代的返回值
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem