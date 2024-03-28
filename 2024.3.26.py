"""
35.搜索插入位置
"""


class Solution(object):
    def binary_search(self, nums, target, start, end):
        if start > end:
            return start
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, end)
        else:
            return self.binary_search(nums, target, start, mid - 1)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target, 0, len(nums) - 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert(nums=[1, 3, 5, 6], target=7))
