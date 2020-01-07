# 归并排序： merge sort
# 分治策略在排序中的应用
# 属于递归算法，将数据表持续分裂为两半，对两半分别进行归并排序

# 传统代码：
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print("Merging", alist)           


# Pythonic的归并排序代码：

def merge_sort(lst):
    # 递归结束条件
    if len(lst) <= 1:
        return lst

    # 分解问题，并递归调用
    middle = len(lst) // 2
    left = merge_sort(lst[:middle]) # 左半部排好序
    right = merge_sort(lst[middle:]) # 右半部排好序
    return merge(left, right)
def merge(left, right):
    # 合并左右半部，完成排序：
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(lst)
print("Merging", lst)    
