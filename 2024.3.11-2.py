"""
1971.寻找图中是否存在路径
并查集版
"""


class DisJointSet:
    def __init__(self, n):
        self.father = [i for i in range(n)]

    def find(self, u):
        if u == self.father[u]:
            return u
        # 路径压缩
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    def is_same(self, u, v):
        return self.find(u) == self.find(v)

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        disjoint_set = DisJointSet(n)
        for u, v in edges:
            disjoint_set.join(u, v)
        return disjoint_set.is_same(source, destination)


if __name__ == '__main__':
    sol = Solution()
    print(sol.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))
