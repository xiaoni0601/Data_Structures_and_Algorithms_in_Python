
# 散列函数设计：
# 1.折叠法(w/隔数反转),eg.62257893--> 62+25+78+93（w/62+52+78+39）=258(w/231)-->258%11(w/231%11=0)=4,因此 4 即为散列值
# 2.平方取中法,eg.54*54=2916-->91%11=3,因此 3 即为散列值
# 3.非数项,eg.字符串cat，-->ord('c')=99,ord('a')=97,ord('t')=116-->99+97+116=313-->313%11=5, 得到散列值5
# 3-2.非数项，+权重因子,eg.cat-->ord('c')=99,ord('a')=97,ord('t')=116-->99*1+97*2+116*3=641-->641%11=3,得到散列值3

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum%tablesize