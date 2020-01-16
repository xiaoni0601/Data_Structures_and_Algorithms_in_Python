# 冲突解决方案： 1.开放定址；2.数据项链。
# 再散列rehashing: newhashvalue = rehash(oldhashvalue)
# for Linear probing: rehash(pos)= (pos + 1) % sizeoftable
# for Skip probing: rehash(pos)=(pos + skip) % sizeoftable, skip 取值为1, 2, 3,....需要注意，避免整除没有余数。
