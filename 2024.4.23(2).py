class Solution(object):
    def minCut(self, s):
        """
        132.分割回文串 II
        动态规划：dp[i] 表示 s[0:i+1] 的最少分割次数。
        :type s: str
        :rtype: int
        """
        # 记录 s[i:j+1] 是否为回文串
        is_palindromic = [[False for _ in range(len(s))] for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if s[i] == s[j]:
                    if i == j or i == j - 1:
                        is_palindromic[i][j] = True
                    else:
                        is_palindromic[i][j] = is_palindromic[i + 1][j - 1]
        # 动态规划
        dp = [i for i in range(len(s))]
        for i in range(1, len(s)):
            if is_palindromic[0][i]:
                dp[i] = 0
                continue
            # 遍历所有的分割点
            for k in range(i):
                # 如果 s[k+1:i+1] 是回文串，意味着可以从 k 开始切割
                if is_palindromic[k+1][i]:
                    dp[i] = min(dp[i], dp[k] + 1)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut(s='aa'))
