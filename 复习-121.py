class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 状态：[持有股票，不持有股票]
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0] = [-prices[0], 0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return max(dp[-1][0], dp[-1][1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
