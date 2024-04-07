class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        100264.最长的严格递增或递减子数组
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        # 递增
        dp1 = [1 for _ in range(len(nums))]
        # 递减
        dp2 = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            dp1[i] = dp1[i - 1] + 1 if nums[i] > nums[i - 1] else 1
            dp2[i] = dp2[i - 1] + 1 if nums[i] < nums[i - 1] else 1
            max_length = max(max_length, dp1[i], dp2[i])
        return max_length


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]))
