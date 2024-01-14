"""
674.最长连续递增序列
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        dp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp += 1
            else:
                dp = 1
            result = max(result, dp)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLengthOfLCIS(nums=[1, 3, 5, 4, 7]))
