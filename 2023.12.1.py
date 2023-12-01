"""
343. 整数拆分
动态规划。
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.integerBreak(n=10))
