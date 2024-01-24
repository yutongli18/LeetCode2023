"""
516.最长回文子序列
"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 1:
                        dp[i][j] = 1
                    elif j - i < 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # 同时加入 s[i] 和 s[j] 不能构成回文子序列，那么看加入哪个能让回文序列更长
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][len(s) - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindromeSubseq(s="cbbd"))
