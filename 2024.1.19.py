"""
115.不同的子序列
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        # 初始化
        for i in range(len(s) + 1):
            dp[i][0] = 1
        # 递推公式
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] if s[i - 1] == t[j - 1] else dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDistinct(s="rabbbit", t="rabbit"))
