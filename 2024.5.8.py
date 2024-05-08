class Solution(object):
    def islandPerimeter(self, grid):
        """
        463. 岛屿的周长
        :type grid: List[List[int]]
        :rtype: int
        """
        cycle_round = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                # 检查每个格子的四条边
                # 有两种情况：在边界上，邻接着水域
                # 检查上边缘
                if i == 0 or grid[i - 1][j] == 0:
                    cycle_round += 1
                # 检查下边缘
                if i == m - 1 or grid[i + 1][j] == 0:
                    cycle_round += 1
                # 检查左边缘
                if j == 0 or grid[i][j - 1] == 0:
                    cycle_round += 1
                # 检查右边缘
                if j == n - 1 or grid[i][j + 1] == 0:
                    cycle_round += 1
        return cycle_round


if __name__ == "__main__":
    sol = Solution()
    print(sol.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
