"""
283.移动零
双指针
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        left, right = 0, 1
        while left < right < len(nums):
            if nums[left] == 0:
                while right < len(nums) and nums[right] == 0:
                    right += 1
                if right >= len(nums):
                    break
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1


if __name__ == '__main__':
    sol = Solution()
    nums = [0]
    sol.moveZeroes(nums)
    print(nums)
