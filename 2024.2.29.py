"""
695.岛屿的最大面积
深度优先搜索 DFS
广度优先搜索 BFS
"""
from collections import deque


class Solution(object):
    def __init__(self):
        # 网格
        self.grid = []
        # 边界条件
        self.x_upper = 0
        self.y_upper = 0
        # 是否遍历
        self.visited = []
        # 四个方向
        self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # （DFS 用）当前岛屿面积
        self.area = 0

    def dfs_area_of_land(self, x, y):
        if x < 0 or x >= self.x_upper or y < 0 or y >= self.y_upper \
                or self.grid[x][y] != 1 or self.visited[x][y]:
            return
        self.visited[x][y] = True
        self.area += 1
        for step in self.steps:
            x, y = x + step[0], y + step[1]
            self.dfs_area_of_land(x, y)
            x, y = x - step[0], y - step[1]
        return

    def bfs_area_of_land(self, x, y):
        area = 1
        queue = deque([(x, y)])
        while queue:
            pos_x, pos_y = queue.popleft()
            for step in self.steps:
                new_x, new_y = pos_x + step[0], pos_y + step[1]
                if 0 <= new_x < self.x_upper and 0 <= new_y < self.y_upper \
                        and self.grid[new_x][new_y] == 1 and not self.visited[new_x][new_y]:
                    area += 1
                    self.visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
        return area

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        # 初始化
        self.grid = grid
        self.x_upper = len(grid)
        self.y_upper = len(grid[0])
        self.visited = [[False for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        # 遍历所有陆地块
        for i in range(self.x_upper):
            for j in range(self.y_upper):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    # self.visited[i][j] = True
                    # max_area = max(max_area, self.bfs_area_of_land(i, j))
                    self.dfs_area_of_land(i, j)
                    max_area = max(max_area, self.area)
                    self.area = 0
        return max_area


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
