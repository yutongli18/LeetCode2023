"""
309.买卖股票的最佳时机含冷冻期
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """# (持有股票，保持卖出股票状态，今天卖出股票，处于冷冻期状态)
        dp = [[0, 0, 0, 0] for _ in range(len(prices))]
        dp[0] = [-prices[0], 0, 0, 0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i], dp[i - 1][3] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]
        print(dp)
        return max(dp[-1])"""
        # (持有股票，不持有股票且处于冷冻期，不持有股票且不处于冷冻期)
        dp = [[0, 0, 0] for _ in range(len(prices))]
        dp[0] = [-prices[0], 0, 0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        print(dp)
        return max(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[1, 4, 2]))
