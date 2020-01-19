
# 树的遍历： 1.前序遍历(根-->左子树-->右子树)；2.中序遍历(左子树-->根-->右子树)；3.后序遍历(左子树-->右子树-->根)
# 递归算法代码实现树的遍历：
# 前序遍历：
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# 中序遍历：
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# 后序遍历：
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


