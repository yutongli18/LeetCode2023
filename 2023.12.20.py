"""
322. 零钱兑换
完全背包 + 组合问题。
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        # 初始化
        for j in range(1, amount + 1):
            dp[0][j] = -1
        # 递推
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    if dp[i][j - coins[i - 1]] == -1:
                        dp[i][j] = dp[i - 1][j]
                    elif dp[i - 1][j] == -1:
                        dp[i][j] = dp[i][j - coins[i - 1]] + 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.coinChange(coins=[186, 419, 83, 408], amount=6249))
