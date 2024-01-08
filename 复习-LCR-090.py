class Solution(object):
    def rob_choice(self, nums, start, end):
        dp = [0 for _ in range(len(nums))]
        dp[start] = nums[start]
        for i in range(start + 1, end + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[end]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_choice(nums=nums, start=0, end=len(nums) - 2),
                   self.rob_choice(nums=nums, start=1, end=len(nums) - 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.rob(nums=[1, 2, 3, 1]))
