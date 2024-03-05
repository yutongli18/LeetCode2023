"""
827.最大人工岛
"""
from collections import deque


class Solution(object):
    def __init__(self):
        # 网格
        self.grid = []
        self.x_upper = 0
        self.y_upper = 0
        # 相连的方向
        self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 当前岛屿面积（DFS用）
        self.curr_area = 0
        # 岛屿面积
        self.island_area = {}
        # 最大岛屿面积
        self.max_area = 0

    # def bfs_lands(self, x, y, sign):
    #     # 遍历的同时，给该岛屿上的所有点打上唯一标记 sign
    #     self.grid[x][y] = sign
    #     # 开始 BFS
    #     area = 1
    #     queue = deque([(x, y)])
    #     while queue:
    #         pos_x, pos_y = queue.popleft()
    #         for step in self.steps:
    #             new_x, new_y = pos_x + step[0], pos_y + step[1]
    #             if 0 <= new_x < self.x_upper and 0 <= new_y < self.y_upper \
    #                     and self.grid[new_x][new_y] == 1:
    #                 self.grid[new_x][new_y] = sign
    #                 area += 1
    #                 queue.append((new_x, new_y))
    #     # 默认的最大岛屿面积是当前的最大岛屿面积
    #     self.max_area = max(self.max_area, area)
    #     return area
    def dfs_lands(self, x, y, sign):
        if x < 0 or x >= self.x_upper or y < 0 or y >= self.y_upper \
                or self.grid[x][y] != 1:
            return
        self.grid[x][y] = sign
        self.curr_area += 1
        for step in self.steps:
            x, y = x + step[0], y + step[1]
            self.dfs_lands(x, y, sign)
            x, y = x - step[0], y - step[1]

    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 初始化
        self.grid = [[num for num in rows] for rows in grid]
        self.x_upper = len(grid)
        self.y_upper = len(grid[0])
        # 遍历一次，记录所有岛屿面积
        sign = 2
        for i in range(self.x_upper):
            for j in range(self.y_upper):
                if self.grid[i][j] == 1:
                    self.island_area.setdefault(sign, 0)
                    # self.island_area[sign] = self.bfs_lands(i, j, sign)
                    self.dfs_lands(i, j, sign)
                    self.island_area[sign] = self.curr_area
                    sign += 1
                    self.curr_area = 0
        # 再遍历一次，对于所有的 0，观察其能够将上下左右四个方向上的哪些不同岛屿连接起来，求总面积
        for i in range(self.x_upper):
            for j in range(self.y_upper):
                if self.grid[i][j] == 0:
                    area = 1
                    signs = []
                    for step in self.steps:
                        new_i, new_j = i + step[0], j + step[1]
                        if 0 <= new_i < self.x_upper and 0 <= new_j < self.y_upper \
                                and self.grid[new_i][new_j] > 0 and self.grid[new_i][new_j] not in signs:
                            area += self.island_area[self.grid[new_i][new_j]]
                            signs.append(self.grid[new_i][new_j])
                    self.max_area = max(self.max_area, area)
        return self.max_area if self.max_area > 0 else self.x_upper * self.y_upper


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestIsland(grid=[[1, 1], [1, 1]]))
