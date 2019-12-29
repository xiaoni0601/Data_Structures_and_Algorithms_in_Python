
#利用双端队列进行回文词判定
from pythonds.basic.deque import Deque

def palchecker(aString): #字符串定义函数
    chardeque = Deque()  #创建双端队列
    
    for ch in aString:   #for循环将字符串aString中每个字符一一提取出来，加入到队列的末尾Rear
        chardeque.addRear(ch)
    
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual: 
        first = chardeque.removeFront() #从队首移除字符
        last = chardeque.removeRear()   #从队尾移除字符
        if first != last:               #判断队首与队尾是否Equal相等
            stillEqual = False
    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))