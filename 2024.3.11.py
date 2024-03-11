"""
1971.寻找图中是否存在路径
DFS 版
"""


class Solution(object):
    def __init__(self):
        self.edges = {}
        self.source = 0
        self.destination = 0
        # 是否访问过
        self.visited = []

    def dfs_path(self, node):
        if node == self.destination:
            return True
        self.visited[node] = True
        for next_node in self.edges[node]:
            if not self.visited[next_node]:
                if self.dfs_path(node=next_node):
                    return True
        return False

    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # 初始化
        for i in range(n):
            self.edges.setdefault(i, [])
        for u, v in edges:
            self.edges[u].append(v)
            self.edges[v].append(u)
        self.source = source
        self.destination = destination
        self.visited = [False for _ in range(n)]
        # 开始遍历
        return self.dfs_path(node=source)


if __name__ == '__main__':
    sol = Solution()
    print(sol.validPath(n=10, edges=[[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]],
                        source=7, destination=5))
