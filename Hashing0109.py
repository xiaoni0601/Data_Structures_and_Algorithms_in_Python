# 散列,散列表：哈希表，hashing table，表中每个存储位置称为槽slot
# 散列函数hash function: 实现从数据项到存储操名称的转换
# 算法复杂度： O(n)
# 一种常用的散列方法：求余数，将数据项除以散列表的大小，得到的余数作为槽号
# 完美散列函数：没有冲突发生，难！
# 退而求其次，近似完美散列函数：冲突最少；计算难度低；充分分散数据项（均匀）


#import hashlib
#print(hashlib.md5("hello world!").hexdigest())
# hashlib使用时出现: Unicode-objects must be encoded before hashing; 
# 解决办法：.encode("utf-8")
import hashlib
hashlib.md5("hello world!".encode("utf-8")).hexdigest()
hashlib.sha1("hello wold!".encode("utf-8")).hexdigest()


import hashlib
m = hashlib.md5()
m.update("hello world!".encode("utf-8"))
m.update("this is part #2".encode("utf-8"))
m.update("this is part #3".encode("utf-8"))
m.hexdigest()