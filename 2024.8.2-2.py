class Solution(object):
    def integerBreak(self, n):
        """
        343.整数拆分
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for k in range(1, i):
                dp[i] = max(dp[i], k * (i - k), k * dp[i - k])
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.integerBreak(10))
