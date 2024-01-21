class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0, 0, 0] for _ in range(len(prices))]
        # 持有股票
        dp[0][0] = -prices[0]
        # 刚刚卖出股票
        dp[0][1] = 0
        # 未持有股票（冷冻期或者一直未持有）
        dp[0][2] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[1, 2, 3, 0, 2]))
