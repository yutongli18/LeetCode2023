"""
518.零钱兑换 II
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 初始化
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        # 递推
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.change(amount=5, coins=[1, 2, 5]))
