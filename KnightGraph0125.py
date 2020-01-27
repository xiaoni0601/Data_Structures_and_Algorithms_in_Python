# 骑士周游问题：
# 1.图表示：棋盘格子作为顶点；
# 2.图搜索算法搜寻路径：走棋步骤作为连接边


# 构建走棋关系图：
from pythonds.graphs import Graph

def knightGraph(bdSize):
    ktGraph = Graph()  # --建立空图
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, column, board_size):
    return (row * board_size) + column


# 合法走棋位置函数：
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   (1, -2),(1,2), (2,-1), (2,1)]  # --马走日 8个格子
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and \
                       legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

# 确认不会走出棋盘位置：
def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False