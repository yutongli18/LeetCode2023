"""
122. 买卖股票的最佳时机 II
贪心算法：关键在于可以把多天股票的收入转换成单天的股票收入之和
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price_diff = [0] * (len(prices) - 1)
        for i in range(0, len(prices) - 1):
            price_diff[i] = prices[i + 1] - prices[i]
        max_count = 0
        for price in price_diff:
            if price > 0:
                max_count += price
        return max_count


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
