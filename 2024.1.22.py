"""
72.编辑距离
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # 初始化
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j
        # 递推公式
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else \
                    min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance(word1='intention', word2='execution'))
