"""
1049.最后一块石头的重量 II
0-1 背包，动态规划。
本质上是把石头分成两个重量接近的堆，然后两个堆相撞（重量相减）。
所以，堆的重量越接近总重量的一半越好。
"""


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        target = int(sum(stones) / 2)
        dp = [[0 for _ in range(target + 1)] for _ in range(len(stones) + 1)]
        for i in range(1, len(stones) + 1):
            for j in range(1, target + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1] if j >= stones[i - 1] else 0)
        return (sum(stones) - dp[-1][-1]) - dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.lastStoneWeightII(stones=[31, 26, 33, 21, 40]))
