class DisJointSet:
    def __init__(self, n):
        self.fathers = [i for i in range(n + 1)]

    def find(self, u):
        """
        找到节点 u 的根节点
        :type u: int
        :rtype: int
        """
        if u == self.fathers[u]:
            return u
        # 路径压缩
        self.fathers[u] = self.find(self.fathers[u])
        return self.fathers[u]

    def is_same(self, u, v):
        """
        判断两个节点是否在同一棵子树上
        :type u: int
        :type v: int
        :rtype: int
        """
        return self.find(u) == self.find(v)

    def join(self, u, v):
        """
        添加一条从节点 u 到节点 v 的边
        :type u: int
        :type v: int
        :rtype: None
        """
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.fathers[v] = u


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        684.冗余连接
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        disjoint_set = DisJointSet(1000)
        for [u, v] in edges:
            if disjoint_set.is_same(u, v):
                return [u, v]
            disjoint_set.join(u, v)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
