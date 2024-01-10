"""
714.买卖股票的最佳时机含手续费
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # （持有股票，不持有股票）
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0] = [-prices[0], 0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return max(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
