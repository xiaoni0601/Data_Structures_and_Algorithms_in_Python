# 快速排序：
# 算法复杂度：O(n log n); O(n) * O(log n)
# 利用‘中值’，将数据表分为大于和小于中值的‘两半’。中值是分裂数据表的目标
# 每部分分别进行快速排序，属于递归算法
# 中值不是中位数，分裂挪动得到，从而分出前半部和后半部。

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:   # --基本结束条件 
        splitpoint = partition(alist, first, last) # --做分裂，快速排序的关键之处。

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last): # --定义分裂函数
    pivotvalue = alist[first]   # 选定“中值”：alist[first]，第一个
    
    # 设置左右标
    leftmark = first + 1 # -左标初值，此时在中值后面相邻的一个
    rightmark = last     # 右标初值
    done = False     # 右标小于左标，done变True
    
    while not done:
        # 左标向右移动：当左标所指的位置数据大于‘中值’，即停止
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        
        # 右标向左移动：当右标所指的位置数据小于‘中值’，即停止
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        
        # 两标相错，移动结束：
        if rightmark < leftmark:
            done = True
        
        else: # 左右标的数值进行交换：
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    
    # 中值就位，位于该处的位置
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    
    #中值点，也是分裂点：
    return rightmark

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)