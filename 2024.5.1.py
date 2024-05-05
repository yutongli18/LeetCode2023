class DisJointSet(object):
    def __init__(self, n):
        self.fathers = [i for i in range(n)]

    def find(self, u):
        """
        找到节点 u 的根节点。
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
        查找节点 u 和节点 v 是否具有相同的根节点。
        :type u: int
        :type v: int
        :rtype: bool
        """
        return self.find(u) == self.find(v)

    def join(self, u, v):
        """
        添加一条从节点 u 到节点 v 的有向边。
        :type u: int
        :type v: int
        :rtype: int
        """
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.fathers[v] = u


class Solution(object):
    def check_circle(self, edges):
        """
        检查当前有向图中是否有环。
        :type edges: list[[int, int]]
        :rtype: list[int, int]
        """
        disjoint_set = DisJointSet(1001)
        for u, v in edges:
            if disjoint_set.is_same(u, v):
                return [u, v]
            disjoint_set.join(u, v)

    def check_valid(self, edges, ignore_idx):
        """
        检查去掉 edges[ignore_idx] 的边之后，是否为一棵有效的有根树。
        :type edges: list[[int, int]]
        :type ignore_idx: int
        :rtype: bool
        """
        disjoint_set = DisJointSet(1001)
        for i in range(len(edges)):
            if i == ignore_idx:
                continue
            if disjoint_set.is_same(edges[i][0], edges[i][1]):
                return False
            disjoint_set.join(edges[i][0], edges[i][1])
        return True

    def findRedundantDirectedConnection(self, edges):
        """
        685.冗余连接 II
        并查集。
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 首先检查入度超过 1 的情况
        abnormal_edges = []
        incoming_dict = [[] for _ in range(1001)]
        for i in range(len(edges)):
            incoming_dict[edges[i][1]].append(i)
            if len(incoming_dict[edges[i][1]]) > 1:
                abnormal_edges = incoming_dict[edges[i][1]]
        if len(abnormal_edges) > 0:
            # 有节点入度超过 1，那么一定要删除其中一条边，优先删除后面的边
            return edges[abnormal_edges[1]] if self.check_valid(edges=edges, ignore_idx=abnormal_edges[1]) \
                else edges[abnormal_edges[0]]
        else:
            # 没有节点的入度超过 1，说明有环
            return self.check_circle(edges=edges)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRedundantDirectedConnection(edges=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
