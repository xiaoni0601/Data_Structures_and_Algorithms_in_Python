# 二叉堆的python实现
# 二叉堆初始化：用列表list来保存；表首为0，占位，实际无用项。
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


# 二叉堆操作的insert():
# 算法复杂度O(n log n)
def insert(self, k):
    self.heapList.append(k)  # -- 添加到末尾
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize) # --新key上浮


def percUp(self, i): ## --定义上浮
    while i // 2 > 0:
        if self.heapList[i] < self.heapList[i // 2]:
            tmp = self.heapList[i // 2]
            # 与父节点交换：
            self.heapList[i // 2] = self.heapList[i]
            self.heapList[i] ] tmp
        i = i // 2 # -- 沿路径向上


# 二叉堆操作的delMin():
def delMin(self):
    retval = self.heapList[1] ## --移走堆顶
    self.heapList[1] = self.heapList[self.currentSize] ## --把最后一个搬到根heaplist[1]
    self.currentSize = self.currentSize - 1  ## -- 最后一个变成倒数第二个(currentSize-1)
    self.heapList.pop()  ## --最后一个pop()掉
    self.percDown(1)  ## --开始纠正堆次序做percDown()，将新顶下沉
    return retval

def percDown(self, i):
    while (i * 2) <= self.currentSize:
        mc = self.minChild(i)
        if self.heapList[i] > self.heapList[mc]:
            tmp = self.heapList[i]
            # 交换下沉：
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = tmp 
        i = mc

def minChild(self, i):
    if i * 2 + 1 > self.currentSize: ## --唯一子节点
        return i * 2  ## --唯一
    else:
        if self.heapList[i * 2] <= self.heapList[i * 2 + 1]:
            return i * 2 ## --返回较小的子节点i*2 (i*2 < i*2+1)
        else:
            return i * 2 + 1  ## --返回较小的子节点i*2+1 (i*2+1 < i*2)


# 二叉堆操作实现buildHeap(lst): 无序表生成“堆”
# 思路：做“下沉”，算法复杂度为0(n)
def buildHeap(self, alist):
    i = len(alist) // 2  # --从最后一个节点的父节点开始； 叶节点无序下沉
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    print(len(self.heapList), i)
    while i > 0:
        print(self.heapList, i)
        self.percDown(i)
        i = i - 1
    print(self.heapList, i)


