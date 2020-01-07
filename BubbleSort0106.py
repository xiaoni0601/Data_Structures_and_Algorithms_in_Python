# 冒泡排序Bubble Sort：
# 多趟，俩俩相邻比较，将最大项就位
# 第一趟n-1数据比较，第二趟n-2数据比较，第n-1趟一定在首位，结束
# 算法复杂度：O(n^2)


def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):  # --n-1 趟
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                # 序错，交换：
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


                # python 也支持直接交换：alist[i],alist[i+1]=alist[i+1],alist[i]
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

# 冒泡算法性能改进：
# 去掉重复过程：


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)
