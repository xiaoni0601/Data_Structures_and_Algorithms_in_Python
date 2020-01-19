# 嵌套列表法

# 创建仅有根节点的二叉树 
def BinaryTree(r):
    return [r, [], []]  # r为根；左右子树分别为[] []

# 将新节点newBranch 插入树root 中作为其直接的左子节点
def insertLeft(root, newBranch): # root为插入对象，在原root上插入newBranch
    t = root.pop(1) # pop(1)为左子树[](从binaryTree的return得到)
    
    if len(t) > 1: # 左子树不为空
        root.insert(1, [newBranch, t, []])  # 1表示插入的位置在左子树，newBranch作为插入的新根，t插入的左子树部分，右子树是空[]
    else:  # 左子树为空
        root.insert(1, [newBranch, [], []])
    return root

# 将新节点newBranch 插入树root 中作为其直接的右子节点
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t]) # 2表示插入的位置在右子树，newBranch作为插入的新根，左子树是空[]，t插入的右子树部分
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root): # --取得根节点的数据项
    return root[0]

def setRootVal(root, newVal): # 将 root[0] set成新的值value
    root[0] = newVal

def getLeftChild(root): # --取得左子树的数据项元素
    return root[1]

def getRightChild(root): # --取得左子树的数据项元素
    return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
R = getRightChild(r)
print(r)
print(l)
print(R)

setRootVal(1, 9)
print(r)

insertLeft(1, 11)
print(r)

print(getRightChild(getRightChild(r)))