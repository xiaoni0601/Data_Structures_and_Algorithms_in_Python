# 词梯问题word ladder： 找到最短的单词变换序列
# 1. 将演变关系表达为 图
# 2. 广度优先搜索BFS，搜寻所有有效路径
# 3. 选择最快到达的路径


# 词梯问题： 1. 图建立表达
# 采用字典dic{}建立桶

from pythonds.graphs import Graph
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter i个字母单词可以属于i个桶
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + ' ' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    
    # add vertices and edges for words un the same bucket同一个桶，单词之间建立边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


# 2. 广度优先搜索 BSF(Breadth First Search)

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def bfs(g, start):   # --起始顶点作为参数
    start.setDistance(0)  # --起始顶点的距离
    start.setPred(None)   # --前驱
    vertQueue = Queue()
    vertQueue.enqueue(start)  # --加入到队列里
    while (vertQueue.size() > 0):  # --只要队列有顶点
        currentVert = vertQueue.dequeue() # -- 取队首作为当前顶点
        for nbr in currentVert.getConnections():  # --遍历邻接顶点
            if (nbr.getColor() == 'white'):  # --邻接顶点是白色的
                nbr.setColor('gray')        # --将邻接顶点改为灰色
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)   # --前驱设为当前顶点
                vertQueue.enqueue(nbr)     # --入队，排到队尾
        currentVert.setColor('black')   # --for循环结束，将当前顶点设为黑色


# 回途追溯函数traverse,确定最短词梯
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


wordgraph = buildGraph("fourletterwords.txt")
bfs(wordgraph,wordgraph.getVertex('FOOL'))
traverse(wordgraph.getVertex('SAGE'))
