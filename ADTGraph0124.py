# 图Graph: 比树tree更为一般的结构，也是由节点和边构成。
# 树，实际是一种具有特殊性质的图
# grapg相关术语：
# 顶点Vertex（也叫节点Node）
# 边Edge（也叫弧Arc，表示两个顶点之间的关系）
# 权重Weight，可以给边edge赋权
# 图G=(V, E)
# ADT Graph的实现：顶点Vertex类
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):   # -- nbr是顶点对象的key
        self.connectedTo[nbr] = weight      # --nbr赋值给权重weight
    
    def __str__(self):   # --字符串化
        return str(self.id) + ' connectedTo: ' 
               + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]



# ADT Graph的实现：图Graph类
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    # 新加顶点：
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    # 通过key查找顶点：
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
     
    def getVertics(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
