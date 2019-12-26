
# 热土豆问题：
# 一群孩子传烫手的热土豆，鼓声停的时候，手里有土豆的小孩就要出列，直到最后一个小孩为止。
from pythonds.basic.queue import Queue
def hotPotato(namelist,num):#参加游戏的人名列表namelist，传num次数
    simqueue = Queue()#创建队列queue
    for name in namelist:
        simqueue.enqueue(name)#队列存放namelist里面参加游戏的人名
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())#传递过程：位于队首的人出列，紧接着从队尾入队。
        simqueue.dequeue()#每一轮移除一次队首的人
    return simqueue.dequeue()#while循环传递num次之后，最终返回最后唯一、剩下的1人

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
print(hotPotato(["Bill","David","Brad","Susan","Jane","Kent"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],5))