"""
188. 买卖股票的最佳时机 IV
最多可以完成 k 笔交易，一共有 2k 种状态。
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(k * 2)] for _ in range(len(prices))]
        # 初始化
        for j in range(k * 2):
            if j % 2 == 0:
                dp[0][j] = -prices[0]
        # 递推公式
        for i in range(1, len(prices)):
            for j in range(k * 2):
                if j == 0:
                    dp[i][j] = max(dp[i - 1][j], -prices[i])
                elif j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        return max([dp[-1][j] for j in range(k * 2)])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(k=2, prices=[2, 1, 4, 5, 2, 9, 7]))
