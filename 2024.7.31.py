class Solution(object):
    def __init__(self):
        self.min_num = 5001

    def binary_min(self, nums, start, end):
        if end < start:
            return self.min_num
        mid = (start + end) // 2
        self.min_num = min(self.min_num, nums[mid])
        if nums[mid] < nums[start]:
            return self.binary_min(nums, start, mid - 1)
        else:
            if nums[mid] > nums[end]:
                return self.binary_min(nums, mid + 1, end)
            else:
                return self.binary_min(nums, start, mid - 1)

    def findMin(self, nums):
        """
        153.寻找旋转排序数组中的最小值
        二分查找
        :type nums: List[int]
        :rtype: int
        """
        return self.binary_min(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))
