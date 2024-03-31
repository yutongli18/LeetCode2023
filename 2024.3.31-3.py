"""
100266.交替子数组计数
"""


class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        left, right = 0, 0
        pre_num = -1
        while right < len(nums):
            if nums[right] == pre_num:
                left = right
            pre_num = nums[right]
            total += (right - left + 1)
            right += 1
        return total


if __name__ == '__main__':
    sol = Solution()
    print(sol.countAlternatingSubarrays(nums=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]))
