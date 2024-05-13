class Solution(object):
    def maxScore(self, grid):
        """
        100281.矩阵中的最大得分
        动态规划？只看首尾。
        :type grid: List[List[int]]
        :rtype: int
        """
        # 最大得分
        max_count = -10 ** 5
        m, n = len(grid), len(grid[0])
        # dp[i][j] 表示到 grid[i][j] 时，起点的最小值
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i < 1 and j < 1:
                    continue
                if i >= 1 and j >= 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], grid[i - 1][j], grid[i][j - 1])
                elif i < 1 and j >= 1:
                    dp[i][j] = min(dp[i][j - 1], grid[i][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j], grid[i - 1][j])
                max_count = max(max_count, grid[i][j] - dp[i][j])
        return max_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore(grid=[[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]))
