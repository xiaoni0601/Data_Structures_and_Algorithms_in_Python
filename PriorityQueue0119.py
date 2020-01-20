# ADT数据结构Binary Heap二叉堆实现优先队列
# BinaryHeap()：创建一个空二叉堆对象
# insert()：将新key加入到堆中
# findMin(): 返回堆中最小项，最小项仍保留在堆中
# delMin():返回堆中最小项，同时从堆中删除
# isEmpty():返回堆是否为空
# size()：返回堆中key的个数
# buildHeap(list):从一个key列表创建新堆

from pythonds.trees.binheap import BinHeap
bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())