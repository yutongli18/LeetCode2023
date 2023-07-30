"""
27. 移除元素
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        left, right = 0, len(nums) - 1
        while left < right:
            while left <= right and nums[left] != val:  # 这里 left <= right 是为了避免 [3, 3] 这种情况
                left += 1
            if left < right:
                while right > left and nums[right] == val:
                    right -= 1
                if right > left:
                    nums[left], nums[right] = nums[right], nums[left]
        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement(nums=[3, 2, 2, 3], val=2))
