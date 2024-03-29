"""
583.两个字符串的删除操作
最长公共子序列。
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if word1[i - 1] == word2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance(word1="sea", word2="eat"))
