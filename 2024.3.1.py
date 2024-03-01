"""
1020.飞地的数量
"""
from collections import deque


class Solution(object):
    def __init__(self):
        # 网格
        self.grid = []
        self.x_upper = 0
        self.y_upper = 0
        # 是否遍历过
        self.visited = []
        # 移动方向
        self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 当前陆地面积
        self.area = 0

    # def bfs_enclaves(self, x, y):
    #     queue = deque([(x, y)])
    #     self.visited[x][y] = True
    #     area = 1
    #     while queue:
    #         pos_x, pos_y = queue.popleft()
    #         for step in self.steps:
    #             new_x, new_y = pos_x + step[0], pos_y + step[1]
    #             if 0 <= new_x < self.x_upper and 0 <= new_y < self.y_upper \
    #                     and self.grid[new_x][new_y] == 1 and not self.visited[new_x][new_y]:
    #                 area += 1
    #                 self.visited[new_x][new_y] = True
    #                 queue.append((new_x, new_y))
    #     return area
    def dfs_enclaves(self, x, y):
        if x < 0 or x >= self.x_upper or y < 0 or y >= self.y_upper \
                or self.grid[x][y] != 1 or self.visited[x][y]:
            return
        self.area += 1
        self.visited[x][y] = True
        for step in self.steps:
            x, y = x + step[0], y + step[1]
            self.dfs_enclaves(x, y)
            x, y = x - step[0], y - step[1]
        return

    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_area = 0
        # 初始化
        self.grid = grid
        self.x_upper, self.y_upper = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        # 首先遍历所有边界上的陆地块，这些不属于飞地面积
        for i in range(self.x_upper):
            if self.grid[i][0] == 1 and not self.visited[i][0]:
                # self.bfs_enclaves(i, 0)
                self.dfs_enclaves(i, 0)
                self.area = 0
            if self.grid[i][self.y_upper - 1] and not self.visited[i][self.y_upper - 1]:
                # self.bfs_enclaves(i, self.y_upper - 1)
                self.dfs_enclaves(i, self.y_upper - 1)
                self.area = 0
        for j in range(self.y_upper):
            if self.grid[0][j] == 1 and not self.visited[0][j]:
                # self.bfs_enclaves(0, j)
                self.dfs_enclaves(0, j)
                self.area = 0
            if self.grid[self.x_upper - 1][j] and not self.visited[self.x_upper - 1][j]:
                # self.bfs_enclaves(self.x_upper - 1, j)
                self.dfs_enclaves(self.x_upper - 1, j)
                self.area = 0
        # 再遍历其它陆地块，它们可以是飞地面积
        for i in range(1, self.x_upper - 1):
            for j in range(1, self.y_upper - 1):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    # total_area += self.bfs_enclaves(i, j)
                    self.dfs_enclaves(i, j)
                    total_area += self.area
                    self.area = 0
        return total_area


if __name__ == '__main__':
    sol = Solution()
    print(sol.numEnclaves(
        grid=[[0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
              [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
              [0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]))
