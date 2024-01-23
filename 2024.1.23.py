"""
647.回文子串
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        # dp[i][j]表示以s[i]开头s[j]结尾的子串是否为回文串
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # 递推公式
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    result += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings(s="abc"))
