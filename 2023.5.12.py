"""
35.搜索插入位置
二分法
"""


def binarySearch(nums, left, right, target):
    mid = int((left + right) / 2)
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        right = mid - 1
        if right < left:
            return mid
        return binarySearch(nums, left, right, target)
    else:
        left = mid + 1
        if left > right:
            return mid + 1
        return binarySearch(nums, left, right, target)


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numLength = len(nums)
        if target > nums[-1]:
            return numLength
        elif target < nums[0]:
            return 0
        else:
            return binarySearch(nums, 0, numLength - 1, target)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert(nums=[1, 3, 5, 6], target=2))
