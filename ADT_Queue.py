class Queue:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):#enqueue()复杂度O(n)
        self.items.insert(0,item)#List首端为队列queue的尾端
    def dequeue(self):#denqueue()复杂度O(1)
        return self.items.pop()#list末端为队列queue的首端
    def size(self):
        return len(self.items)