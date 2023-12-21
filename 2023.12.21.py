"""
279.完全平方数
动态规划：完全背包。
"""


class Solution(object):
    def __init__(self):
        self.nums = []

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 可选平方数列表
        i = 1
        while i ** 2 <= n:
            self.nums.append(i ** 2)
            i += 1
        m = len(self.nums)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 初始化
        for j in range(1, n + 1):
            dp[0][j] = float("inf")
        # 递推
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j >= self.nums[i - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - self.nums[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(n=12))
