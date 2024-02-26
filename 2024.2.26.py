"""
797.所有可能的路径
"""


class Solution(object):
    def __init__(self):
        # 所有路径
        self.paths = []
        # 当前路径
        self.path = [0]
        # 有向无环图
        self.graph = []
        # 节点总数
        self.n = 0

    def dfs_traverse(self, i):
        # 终止条件
        if i == self.n - 1:
            self.paths.append(self.path[:])
            return
        # 递归当前节点的所有路径
        for sub_i in self.graph[i]:
            self.path.append(sub_i)
            self.dfs_traverse(sub_i)
            self.path.pop()
        return

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graph = graph[:]
        self.n = len(graph)
        self.dfs_traverse(0)
        return self.paths[:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
