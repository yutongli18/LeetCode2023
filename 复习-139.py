class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for j in range(1, len(s) + 1):
            for i in range(0, j):
                dp[j] |= (dp[i] and s[i:j] in wordDict)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
