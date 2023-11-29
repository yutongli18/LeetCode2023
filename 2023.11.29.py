"""
62. 不同路径
确实用回溯法可解，但是会超时。
动态规划：注意初始化，其实 dp 数组的第一行和第一列都可以直接初始化（因为都是 1 ），这样就可以避开 i - 1 和 j - 1 的有效性检测问题了。
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        """dp[0][1], dp[1][0] = 1, 1
        for i in range(m):
            if i == 0:
                start_j = 2
            elif i == 1:
                start_j = 1
            else:
                start_j = 0
            for j in range(start_j, n):
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if j - 1 >= 0:
                        dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]"""
        # 这里：初始化的方法
        for i in range(1, m):
            dp[i][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
        # 动态规划
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(m=1, n=2))
