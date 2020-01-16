class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

# put()实现
def hashfunction(self, key):
    return key % self.size
def rehash(self, oldhash):
    return (oldhash + 1) % self.size
    
def put(self, key, data):
    hashvalue = self.hashfunction(key)

# key不存在，未冲突
if self.slots[hashvalue] == None:
    self.slots[hashvalue] = key 
    self.data[hashvalue] = data   
else:
    # key已经存在，替换value：
    if self.slots[hashvalue] == key:
        self.data[hashvalue] = data   
    else:
        nextslot = self.rehash(hashvalue)
        # 散列冲突，再散列rehash，直到找到空槽或者key
        while self.slots[nextslot] != None and \
            self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot)
        
        
        if self.slots[nextslot] == None:
            self.slots[nextslot] = key
            self.data[nextslot] = data
        else:
            self.data[nextslot] = data


# get() 实现
def get(self, key):
    # 标记散列值为查找起点：
    startslot = self.hashfunction(key)
    
    data = None
    stop = False
    found = False
    position = startslot

    # 查找key，直到空槽或回到起点
    while self.slots[position] != None and \
        not found and not stop:
        if self.slots[position] == key:
            found = True
            data = self.data[position]
        else:
            # 微找到key，再散列rehash继续找：
            position = self.rehash(position)
            if position == startslot:
                stop = True  # 回到起点，停
    return data

# 通过特殊方法实现[]访问：
def __getitem__(self, key):
    return self.get(key)

def __setitem__(self, key, data):
    self.put(key, data)
