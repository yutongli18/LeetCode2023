"""
463.岛屿的周长
"""
from collections import deque


class Solution(object):
    # def __init__(self):
    #     # 网格区域
    #     self.grid = []
    #     self.x_upper = 0
    #     self.y_upper = 0
    #     # 是否遍历过
    #     self.visited = []
    #     # 四个遍历方向
    #     self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    #     # 岛屿的周长
    #     self.perimeter = 0

    # def bfs_island(self, x, y):
    #     self.visited[x][y] = True
    #     queue = deque([(x, y)])
    #     while queue:
    #         pos_x, pos_y = queue.popleft()
    #         for step in self.steps:
    #             new_x, new_y = pos_x + step[0], pos_y + step[1]
    #             if new_x < 0 or new_x >= self.x_upper or new_y < 0 or new_y >= self.y_upper \
    #                     or self.grid[new_x][new_y] == 0:
    #                 self.perimeter += 1
    #             elif not self.visited[new_x][new_y]:
    #                 self.visited[new_x][new_y] = True
    #                 queue.append((new_x, new_y))

    # def dfs_island(self, x, y):
    #     if x < 0 or x >= self.x_upper or y < 0 or y >= self.y_upper \
    #             or self.grid[x][y] == 0:
    #         self.perimeter += 1
    #         return
    #     elif self.visited[x][y]:
    #         return
    #     self.visited[x][y] = True
    #     for step in self.steps:
    #         x, y = x + step[0], y + step[1]
    #         self.dfs_island(x, y)
    #         x, y = x - step[0], y - step[1]

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # # 初始化
        # self.grid = grid
        # self.x_upper, self.y_upper = len(grid), len(grid[0])
        # self.visited = [[False for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        # # 遍历
        # for i in range(self.x_upper):
        #     for j in range(self.y_upper):
        #         if self.grid[i][j] == 1:
        #             # self.bfs_island(i, j)
        #             self.dfs_island(i, j)
        #             return self.perimeter
        # return 0
        # 因为岛屿只有一个，不需要区分，所以可以直接计算周长
        perimeter = 0
        steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        i_upper, j_upper = len(grid), len(grid[0])
        for i in range(i_upper):
            for j in range(j_upper):
                if grid[i][j] == 1:
                    for step in steps:
                        new_i, new_j = i + step[0], j + step[1]
                        if new_i < 0 or new_i >= i_upper or new_j < 0 or new_j >= j_upper \
                                or grid[new_i][new_j] == 0:
                            perimeter += 1
        return perimeter


if __name__ == '__main__':
    sol = Solution()
    print(sol.islandPerimeter(grid=[[1]]))
