"""
122. 买卖股票的最佳时机 II
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0, -prices[0]]]
        for i in range(1, len(prices)):
            val1 = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            val2 = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp.append([val1, val2])
        return dp[-1][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))
