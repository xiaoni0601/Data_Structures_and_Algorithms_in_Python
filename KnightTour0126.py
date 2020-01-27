# 骑士周游算法实现
def knightTour(n, path, u, limit): # --n表示层次；path表示路径；u表示当前顶点；limit表示搜索总深度
    u.setColor('gray')
    path.append(u)   # --将当前顶点加入路径
    if n < limit:
        nbrList = list(u.getConnections())  # --将所有合法移动逐一深入
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':  # --选择白色未经过的顶点深入
                done = knightTour(n+1, path, nbrList[i], limit)  # --层次+1，递归深入
            i = i + 1
        if not done: # --prepare to backtrack,尝试本层下一个顶点
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done



# 骑士周游算法改进：

# 修改遍历下一格的次序：将u的合法移动目标棋盘格排序为具有最少合法移动目标的格子优先搜索
# 采用先验的知识来改进算法性能，称为启发式规则heuristic
# heuristic，有效减小搜索范围，更快达到目标
# 例如，黑白棋中的’金角银边‘口诀，指导程序优先占边角位置
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append(c, v)
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]