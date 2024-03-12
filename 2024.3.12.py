"""
684.冗余连接
并查集
"""


class DisJointSet(object):
    def __init__(self, n):
        self.father = [u for u in range(n)]

    def find(self, u):
        if u == self.father[u]:
            return u
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
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = 0
        for edge in edges:
            n = max(n, edge[0], edge[1])
        disjoint_set = DisJointSet(n)
        for u, v in edges:
            if disjoint_set.is_same(u - 1, v - 1):
                return [u, v]
            disjoint_set.join(u - 1, v - 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
