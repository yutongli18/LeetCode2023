"""
33.搜索旋转排序数组
二分查找
"""


def binarySearch(nums, left, right, target):
    if left > right:
        return -1
    # print(left, right)
    mid = int((left + right) / 2)
    if target == nums[mid]:
        return mid
    seg = 0
    if nums[mid] < nums[0]:  # 表示mid落在原来的前半段，现在旋转后的后半段里了
        seg = 1
    if target > nums[mid]:
        if seg == 1:
            if target > nums[-1]:
                return binarySearch(nums, left, mid - 1, target)
            else:
                return binarySearch(nums, mid + 1, right, target)
        else:
            return binarySearch(nums, mid + 1, right, target)

    else:
        if seg == 0:
            if target < nums[0]:
                return binarySearch(nums, mid + 1, right, target)
            else:
                return binarySearch(nums, left, mid - 1, target)
        else:
            return binarySearch(nums, left, mid - 1, target)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return binarySearch(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    sol = Solution()
    print(sol.search(nums=[1, 3], target=2))
