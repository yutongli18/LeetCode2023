"""
704.二分查找
注意两种区间的划分
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numsLength = len(nums)
        left, right = 0, numsLength-1
        while 0 <= left < numsLength and 0 <= right < numsLength and left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
