"""
34.在排序数组中查找元素的第一个和最后一个位置
"""


class Solution(object):
    def binary_search(self, nums, target, start, end):
        if start > end:
            return -1
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, end)
        else:
            return self.binary_search(nums, target, start, mid - 1)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0 or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        index = self.binary_search(nums, target, 0, len(nums) - 1)
        if index < 0:
            return [-1, -1]
        start, end = index, index
        while start >= 0 and nums[start] == target:
            start -= 1
        while end < len(nums) and nums[end] == target:
            end += 1
        return [start + 1, end - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
