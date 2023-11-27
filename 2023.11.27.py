"""
70.爬楼梯
动态规划。
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(n=3))
