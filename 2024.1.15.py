"""
1143.最长公共子序列
和子数组的区别在于子序列不需要是连续的，所以在 text1[i - 1] != text2[j - 1] 时，还可以往前考虑。
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        # 递推公式
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if text1[i - 1] == text2[j - 1] \
                    else max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonSubsequence(text1="abcde", text2="ace"))
