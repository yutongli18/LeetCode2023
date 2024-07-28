from collections import deque


class Solution(object):
    def __init__(self):
        self.graph = []
        self.colors = []

    def DFSColor(self, c_id, color):
        self.colors[c_id] = color
        if color == 0:
            n_color = 1
        else:
            n_color = 0
        for n_id in self.graph[c_id]:
            if self.colors[n_id] == -1:
                if not self.DFSColor(n_id, n_color):
                    return False
            if self.colors[n_id] == self.colors[c_id]:
                return False
        return True

    def BFSColor(self, r_id):
        self.colors[r_id] = 0
        queue = deque([r_id])
        while len(queue) > 0:
            c_id = queue.popleft()
            if self.colors[c_id] == 0:
                n_color = 1
            else:
                n_color = 0
            for n_id in self.graph[c_id]:
                if self.colors[n_id] == -1:
                    self.colors[n_id] = n_color
                    queue.append(n_id)
                elif self.colors[n_id] == self.colors[c_id]:
                    return False
        return True

    def isBipartite(self, graph):
        """
        785.判断二分图
        :type graph: List[List[int]]
        :rtype: bool
        """
        # 初始化
        self.graph = [[num for num in row] for row in graph]
        num_points = len(graph)
        self.colors = [-1 for _ in range(num_points)]
        # DFS染色
        # for c_id in range(num_points):
        #     if self.colors[c_id] == -1:
        #         if not self.DFSColor(c_id, 0):
        #             return False
        # return True
        # BFS染色
        for c_id in range(num_points):
            if self.colors[c_id] == -1:
                if not self.BFSColor(c_id):
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isBipartite(
        [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
         [2, 4, 5, 6, 7, 8]]))
