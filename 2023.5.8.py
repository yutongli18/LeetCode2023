"""
27.移除元素
双指针。
如果不保留原来数组中的所有元素（直接把right对应的，符合条件的值复制到left上），会比现在的方法要简单。
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numLength = len(nums)
        left, right = 0, numLength - 1
        while left < right:
            while left < right and nums[left] != val:
                left += 1
            if nums[left] == val:
                while right > left and nums[right] == val:
                    right -= 1
                if nums[right] != val:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
        if left < numLength and nums[left] != val:
            left += 1
        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement(nums=[2], val=3))
