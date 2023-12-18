"""
474.一和零
动态规划：0-1 背包
"""


from collections import Counter


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strs_list = []
        for s in strs:
            s_counter = Counter(s)
            strs_list.append([s_counter["0"], s_counter["1"]])
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= strs_list[i - 1][0] and k >= strs_list[i - 1][1]:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - strs_list[i - 1][0]][k - strs_list[i - 1][1]] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[-1][-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxForm(strs=["10", "0", "1"], m=1, n=1))
