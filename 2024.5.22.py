class Solution(object):
    def maxSubArray(self, nums):
        """
        53.最大子数组和
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        dp = [num for num in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray(nums=[5, 4, -1, 7, 8]))
