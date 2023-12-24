class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        bag_size = sum(stones) // 2
        n = len(stones)
        # 初始化
        dp = [0 for _ in range(bag_size + 1)]
        dp[0] = 0
        # 递推
        for i in range(n):
            for j in range(bag_size, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return abs(dp[-1] - (sum(stones) - dp[-1]))


if __name__ == '__main__':
    sol = Solution()
    print(sol.lastStoneWeightII(stones=[2, 7, 4, 1, 8, 1]))
