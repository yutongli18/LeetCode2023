class Solution(object):
    def longestPalindrome(self, s):
        """
        5.最长回文子串
        动态规划。
        注意子串必须是连续的。
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        max_length = 1
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j, -1, -1):
                # 长度为1的串必然是回文子串
                if j == i:
                    dp[i][j] = 1
                # 长度为2的串需要单独处理
                # 如果两个元素相等，说明是回文子串
                elif j == i + 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                # 对于其它情况
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] > 0:
                        dp[i][j] = dp[i+1][j-1] + 2
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    start, end = i, j
        return s[start:end+1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome(s="cbbd"))
