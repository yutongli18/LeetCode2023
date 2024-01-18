class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        if p1 >= len(s):
            return True
        else:
            return False"""
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if s[i - 1] == t[j - 1] else dp[i][j - 1]
        return dp[-1][-1] == len(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence(s="axc", t="ahbgdc"))
