class DisJointSet:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.total = [-1 for _ in range(n)]

    def find(self, u):
        if self.father[u] == u:
            return u
        # 路径压缩
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    def is_same(self, u, v):
        return self.find(u) == self.find(v)

    def join(self, u, v, weight):
        u = self.find(u)
        v = self.find(v)
        # 这里：即使 u 和 v 已经在一个并查集内了，但是新来的边的权重也要添加到并查集的总权重中
        self.total[u] = self.total[u] & weight
        if u == v:
            return
        self.father[v] = u
        # 这里：如果 u 和 v 的父节点不同，意味着要将 u 和 v 的两个并查集合并，所以它们的权重也要合并
        self.total[u] = self.total[u] & self.total[v]


class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        100244.带权图里旅途的最小代价
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        disjoint_set = DisJointSet(n)
        for start, end, weight in edges:
            disjoint_set.join(start, end, weight)
        answer = []
        for start, end in query:
            if start == end:
                answer.append(0)
            elif not disjoint_set.is_same(start, end):
                answer.append(-1)
            else:
                answer.append(disjoint_set.total[disjoint_set.find(start)])
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumCost(n=3, edges=[[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], query=[[1, 2]]))
