
#链表实现：add； size； search； remove

class UnorderedList:
    def __init__(self):
        self.head = None

mylist = UnorderedList()
print(mylist.head)

#do add
def add(self,item):
    temp = Node(item)##将item生成节点Node，然后将节点Node命名为临时变量temp
    temp.setNext(self.head)
    self.head = temp

#do size
def size(self):
    current = self.head
    count = 0
    while current != None:
        count = count + 1
        current = current.getNext()
    return count

#do search
def search(self,item):
    current = self.head
    found =False
    while current != None and not found:
        if current.getData() == item:
            found = True
        else:
            current = current.getNext()
    return found


#do remove
def remove(self,item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current.getData() == item:
            found = True
        else:
            previous = current
            current = current.getNext()
    if previous == None:
        self.head = current.getNext()
    else:
        previous.setNext(current.getNext())
