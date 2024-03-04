"""
417.太平洋大西洋水流问题
"""


# from collections import deque


class Solution(object):
    def __init__(self):
        # 岛屿网格
        self.heights = []
        self.x_upper = 0
        self.y_upper = 0
        # 是否遍历过
        self.visited = []
        # 四个流动方向
        self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 对两个大洋的流入情况：(P, A)
        self.reach = []

    def dfs(self, x, y, is_pacific):
        self.visited[x][y] = True
        if is_pacific:
            self.reach[x][y][0] = True
        else:
            self.reach[x][y][1] = True
        height = self.heights[x][y]
        for step in self.steps:
            x, y = x + step[0], y + step[1]
            if 0 <= x < self.x_upper and 0 <= y < self.y_upper \
                    and self.heights[x][y] >= height and not self.visited[x][y]:
                self.dfs(x, y, is_pacific)
            x, y = x - step[0], y - step[1]

    # def bfs(self, x, y, isPacific):
    #     self.visited[x][y] = True
    #     if isPacific:
    #         self.reach[x][y][0] = True
    #     else:
    #         self.reach[x][y][1] = True
    #     queue = deque([(x, y)])
    #     while queue:
    #         pos_x, pos_y = queue.popleft()
    #         for step in self.steps:
    #             new_x, new_y = pos_x + step[0], pos_y + step[1]
    #             if 0 <= new_x < self.x_upper and 0 <= new_y < self.y_upper \
    #                     and self.heights[new_x][new_y] >= self.heights[pos_x][pos_y] and not self.visited[new_x][new_y]:
    #                 self.visited[new_x][new_y] = True
    #                 if isPacific:
    #                     self.reach[new_x][new_y][0] = self.reach[pos_x][pos_y][0]
    #                 else:
    #                     self.reach[new_x][new_y][1] = self.reach[pos_x][pos_y][1]
    #                 queue.append((new_x, new_y))

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # 初始化
        self.heights = heights
        self.x_upper, self.y_upper = len(heights), len(heights[0])
        self.visited = [[False for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        self.reach = [[[False, False] for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        # 逆流遍历“太平洋”
        for i in range(self.x_upper):
            # self.bfs(i, 0, True)
            self.dfs(i, 0, True)
        for j in range(self.y_upper):
            # self.bfs(0, j, True)
            self.dfs(0, j, True)
        self.visited = [[False for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        # 逆流遍历“大西洋”
        for i in range(self.x_upper):
            # self.bfs(i, self.y_upper - 1, False)
            self.dfs(i, self.y_upper - 1, False)
        for j in range(self.y_upper):
            # self.bfs(self.x_upper - 1, j, False)
            self.dfs(self.x_upper - 1, j, False)
        # 结果集合
        results = []
        for i in range(self.x_upper):
            for j in range(self.y_upper):
                if self.reach[i][j][0] and self.reach[i][j][1]:
                    results.append([i, j])
        return results


if __name__ == '__main__':
    sol = Solution()
    print(sol.pacificAtlantic(heights=[[1, 2, 2, 3, 5],
                                       [3, 2, 3, 4, 4],
                                       [2, 4, 5, 3, 1],
                                       [6, 7, 1, 4, 5],
                                       [5, 1, 1, 2, 4]]))
