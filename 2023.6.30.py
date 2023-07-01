"""
35.搜索插入位置
二分查找
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numsLength = len(nums)
        left, right = 0, numsLength - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert(nums=[1, 3, 5, 6], target=7))
