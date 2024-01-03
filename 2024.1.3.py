class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 四状态：(第一次不持有, 第一次持有, 第二次不持有, 第二次持有)
        dp = [[0, -prices[0], 0, -prices[0]]]
        for i in range(1, len(prices)):
            val1 = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            val2 = max(dp[i - 1][1], -prices[i])
            val3 = max(dp[i - 1][2], dp[i - 1][3] + prices[i])
            val4 = max(dp[i - 1][3], dp[i - 1][0] - prices[i])
            dp.append([val1, val2, val3, val4])
        return max(val for val in dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[1, 2, 3, 4, 5]))
