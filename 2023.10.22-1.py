class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_sum = 153
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[j] > nums[i] and nums[j] > nums[k]:
                        min_sum = min(min_sum, nums[i] + nums[j] + nums[k])
        return min_sum if min_sum < 153 else -1
