class Solution(object):
    def __init__(self):
        self.grid = []
        self.m = 0
        self.n = 0
        self.visited = []
        self.steps = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.count = 0

    def dfs(self, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n or self.grid[x][y] != "1" or self.visited[x][y]:
            return
        self.visited[x][y] = True
        for step_x, step_y in self.steps:
            self.dfs(x + step_x, y + step_y)
        return

    def numIslands(self, grid):
        """
        200.岛屿数量
        DFS
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = [[flag for flag in grid_row] for grid_row in grid]
        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1" and not self.visited[i][j]:
                    self.count += 1
                    self.dfs(i, j)
        return self.count


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands(grid=[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
                               ["0", "0", "0", "1", "1"]]))
