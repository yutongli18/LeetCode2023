"""
34. 在排序数组中查找元素的第一个和最后一个位置
二分查找。
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        startIndex, endIndex = -1, -1
        numsLength = len(nums)
        left, right = 0, numsLength - 1
        # 求开始位置
        while left < numsLength and right >= 0 and left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                startIndex = mid  # 这里不需要做最小值判断，因为查找的过程是一直向左的
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = 0, numsLength - 1
        # 求结束位置
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                endIndex = mid  # 同理，这里也不需要做最大值判断
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [startIndex, endIndex]


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
