class Solution(object):
    def maximumTotalCost(self, nums):
        """
        100337.最大化子数组的总成本
        贪心？贪心解决不了出现连续负数的情况。
        状态动态规划：每个时间步 i 计算两种状态。
        :type nums: List[int]
        :rtype: int
        """
        # MIN_NUM = (-10 ** 9 - 1) * len(nums)
        # dp = [[MIN_NUM for _ in range(len(nums))] for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     dp[i][0] = 0
        #     for j in range(i + 1):
        #         dp[i][0] += (-1) ** j * nums[j]
        # for i in range(1, len(nums)):
        #     for j in range(1, i + 1):
        #         # dp[i][j] 表示到 nums[i] 为止的最大成本，上一个分割点为 nums[j]
        #         dp[i][j] = max(dp[j - 1])
        #         for k in range(j, i + 1):
        #             dp[i][j] += (-1) ** (k - j) * nums[k]
        # # print(dp)
        # return max(dp[len(nums) - 1])
        MIN_INT = (-10 ** 9 - 1) * len(nums)
        # dp = [符号为 + 时的前缀和，符号为 - 时的前缀和]
        dp = [nums[0], MIN_INT]
        for num in nums[1:]:
            temp_0 = max(dp[0], dp[1]) + num
            temp_1 = dp[0] - num
            dp[0], dp[1] = temp_0, temp_1
        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumTotalCost(nums=[1, -1, 1, -1]))
