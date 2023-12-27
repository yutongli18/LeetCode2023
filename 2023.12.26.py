"""
198.打家劫舍
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.rob(nums=[2, 7, 9, 3, 1]))
