"""
63.不同路径 II
动态规划：注意如何处理障碍物能比较高效。
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 初始化
        for i in range(m):
            # dp[i][0] = 1 if obstacleGrid[i][0] != 1 and dp[i - 1][0] != 0 else 0
            # if obstacleGrid[i][0] == 1:
            #     dp[i][0] = 0
            # else:
            #     if i == 0:
            #         dp[i][0] = 1
            #     elif dp[i - 1][0] != 0:
            #         dp[i][0] = 1
            #     else:
            #         dp[i][0] = 0
            # dp[i][0] = 0 if obstacleGrid[i][0] == 1 or (i > 0 and dp[i - 1][0] == 0) else 1
            # 这里：当有一个障碍的时候，后面的位置就都不可达了，直接用原来的初始值 0 就行
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            # dp[0][j] = 1 if obstacleGrid[0][j] != 1 and dp[0][j - 1] != 0 else 0
            # if obstacleGrid[0][j] == 1:
            #     dp[0][j] = 0
            # else:
            #     if j == 0:
            #         dp[0][j] = 1
            #     elif dp[0][j - 1] != 0:
            #         dp[0][j] = 1
            #     else:
            #         dp[0][j] = 0
            # dp[0][j] = 0 if obstacleGrid[0][j] == 1 or (j > 0 and dp[0][j - 1] == 0) else 1
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                # if obstacleGrid[i][j] == 1:
                #     dp[i][j] = 0
                # else:
                #     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                # 这里：反正之前初始化的时候就是初始化为 0。当不满足条件的时候直接跳过就行了，不需要再赋值一遍 0
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid=[[0, 0]]))
