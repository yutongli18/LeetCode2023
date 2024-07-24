class Solution(object):
    def binary_search(self, nums, target, left, right):
        if left > right:
            return left
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, target, left, mid - 1)
        else:
            return self.binary_search(nums, target, mid + 1, right)

    def searchInsert(self, nums, target):
        """
        35.搜索插入位置
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert(nums=[1, 3, 5, 6], target=7))
