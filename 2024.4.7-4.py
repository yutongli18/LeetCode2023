from collections import deque


class Solution(object):
    def __init__(self):
        self.n = 1  # 节点数
        self.edge_dict = {}  # 以 key 为起点的终点集合：[[dest, weight]]
        self.node_idx = []  # 节点对应的连通块编号
        self.total = []  # 每个连通快对应的边与运算总结果

    def bfs(self, start, idx):
        self.node_idx[start] = idx
        self.total.append(-1)
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in self.edge_dict.keys():
                continue
            for dest, weight in self.edge_dict[node]:
                # 因为边可以重复经过
                self.total[idx] = self.total[idx] & weight if self.total[idx] >= 0 else weight
                # 节点本身不能被重复遍历，否则会无限循环无法退出
                if self.node_idx[dest] < 0:
                    self.node_idx[dest] = idx
                    queue.append(dest)

    def minimumCost(self, n, edges, query):
        """
        100244.带权图里旅途的最小代价
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        # 初始化
        self.n = n
        self.node_idx = [-1 for _ in range(n)]
        for start, end, weight in edges:
            self.edge_dict.setdefault(start, [])
            self.edge_dict[start].append([end, weight])
            self.edge_dict.setdefault(end, [])
            self.edge_dict[end].append([start, weight])
        # 执行 BFS 为所有连通块打编号
        index = 0
        for i in range(n):
            if self.node_idx[i] < 0:
                self.bfs(i, index)
                index += 1
        # 返回结果
        answer = []
        for start, end in query:
            if start == end:
                answer.append(0)
            elif self.node_idx[start] != self.node_idx[end]:
                answer.append(-1)
            else:
                answer.append(self.total[self.node_idx[start]])
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumCost(n=3, edges=[[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], query=[[1, 2]]))
