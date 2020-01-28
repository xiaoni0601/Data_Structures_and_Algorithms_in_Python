# 最短路径问题：
# Dijkstra算法
# Dijkstra算法用于解决带权图的最短路径问题；只能处理权重大于0的权重


from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(aGraph, start):
    pq = PriorityQueue()  # 
    start.setDistance(0)  # --开始顶点距离设置为0
    pq.buildHeap([(v.getDistance(),v) for v in aGraph]) # --对所有顶点建堆，形成优先队列
    while not pq.isEmpty():
        currentVert = pq.delMin()  # --当前顶点出堆
        for nextVert in cuttentVert.getConnections():  # --所有连接的顶点进行距离更新
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)  # --当前顶点的距离+权重值作为新顶点的距离
                    if newDist < nextVert.getDistance():
                        nextVert.setDistance( newDist )
                        nextVert.setPred(currentVert)
                        pq.decreaseKey(nextVert, newDist)
        