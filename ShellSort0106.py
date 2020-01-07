# 谢尔排序 shell sort: 
# 以插入排序insertion sort 为基础，对无序表进行间隔划分子列表

def shellSort(alist):
    sublistcount = len(alist) // 2 # 间隔设定

    while sublistcount > 0:
        for startposition in range(sublistcount):   # 子列表排序
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2 # 间隔缩小
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)

        