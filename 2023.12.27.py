"""
213. 打家劫舍 II
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]
        # 初始化
        dp1[1] = nums[0]
        dp2[1] = nums[1]
        # 递推
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 1])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return max(dp1[-1], dp2[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.rob(nums=[1, 2, 3, 1]))
