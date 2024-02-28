"""
200.岛屿数量
深度优先搜索 DFS
"""


class Solution(object):
    def __init__(self):
        # 网格
        self.grid = []
        # 是否遍历过
        self.visited = []
        # 边界条件
        self.x_upper = 0
        self.y_upper = 0
        # 四个遍历方向
        self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs_lands(self, x, y):
        for step in self.steps:
            x, y = x + step[0], y + step[1]
            if 0 <= x < self.x_upper and 0 <= y < self.y_upper \
                    and self.grid[x][y] == "1" and not self.visited[x][y]:
                self.visited[x][y] = True
                self.dfs_lands(x, y)
            x, y = x - step[0], y - step[1]
        return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        self.grid = grid
        self.x_upper, self.y_upper = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        for x in range(self.x_upper):
            for y in range(self.y_upper):
                if self.grid[x][y] == "1" and not self.visited[x][y]:
                    self.visited[x][y] = True
                    count += 1
                    self.dfs_lands(x, y)
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands(grid=[["1", "1", "0", "0", "0"],
                               ["1", "1", "0", "0", "0"],
                               ["0", "0", "1", "0", "0"],
                               ["0", "0", "0", "1", "1"]]))
