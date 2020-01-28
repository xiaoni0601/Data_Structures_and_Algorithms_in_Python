# 强连通分支Strongly Connected Components：在图中发现高度聚集节点群的算法
# 强连通分支，定义为图G的一个子集C
# 转置概念Transposition
# 算法1：Kosaraju算法
# Kosaraju算法思路：
# 1.调用DFS算法计算每个顶点的“结束时间” -->
# 2.将G转置得到GT-->
# 3.按照结束时间倒序对GT调用DFS-->
# 4.森林中的每棵树就是一个强连通分支