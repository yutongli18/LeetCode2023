"""
685.冗余连接II
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
    def checkTree(self, n, edges, delete_edge):
        """
        判断一张图是不是一棵树
        :param n: 节点数
        :param edges: 边集合
        :return: boolean
        """
        disjoint_set = DisJointSet(n + 1)
        for u, v in edges:
            if u == delete_edge[0] and v == delete_edge[1]:
                continue
            if disjoint_set.is_same(u, v):
                return False
            disjoint_set.join(u, v)
        return True

    def remove_connection(self, n, edges):
        """
        在有向图上找环
        :param n: 节点数
        :param edges: 边集合
        :return: [int, int]
        """
        disjoint_set = DisJointSet(n + 1)
        for u, v in edges:
            if disjoint_set.is_same(u, v):
                return [u, v]
            disjoint_set.join(u, v)

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 判断节点数
        n = 0
        for u, v in edges:
            n = max(n, u, v)
        # 第一种情况：节点的入度为 2
        father = [u for u in range(n + 1)]
        redundant_list = []
        for u, v in edges:
            if father[v] == v:
                father[v] = u
            else:
                redundant_list.append([father[v], v])
                redundant_list.append([u, v])
                break
        if redundant_list:
            return redundant_list[0] if not self.checkTree(n, edges, delete_edge=redundant_list[1]) \
                else redundant_list[1]
        # 第二种情况：出现了环路
        return self.remove_connection(n, edges)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRedundantDirectedConnection(edges=[[2, 1], [3, 1], [4, 2], [1, 4]]))
