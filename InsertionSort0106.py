# 插入排序，如扑克牌

def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index] # 待插入项/新项 alist[index]
        position = index            # 待插入项挪出来之后，它原来的位置同时也空了出来

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
        
        alist[position] = currentvalue # 插入新项
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)           