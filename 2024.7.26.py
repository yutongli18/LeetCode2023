class Solution(object):
    def __init__(self):
        self.nums = []
        self.target = 0

    # def binary_search(self, start, end, is_left=False):
    #     if end < start:
    #         return -1
    #     if end - start <= 1 and self.nums[start] == self.target:
    #         # 这里的判断超级麻烦，原因在于找右边界的时候，按照当前二分查找的逻辑，[8, 10]的情况会导致死循环
    #         # self.nums[start] == self.target是为了处理找不到的情况
    #         if is_left:
    #             # 左边界的话，考虑[2, 2]的情况
    #             return start
    #         else:
    #             # self.nums[end] == self.target处理[2, 2]的情况
    #             return end if self.nums[end] == self.target else start
    #     mid = (start + end) // 2
    #     if self.nums[mid] == self.target:
    #         # 这里保留了mid作为边界，这是产生上面复杂判断条件的根源
    #         if is_left:
    #             return self.binary_search(start, mid, is_left)
    #         else:
    #             return self.binary_search(mid, end, is_left)
    #     elif self.nums[mid] > self.target:
    #         return self.binary_search(start, mid - 1, is_left)
    #     else:
    #         return self.binary_search(mid + 1, end, is_left)
    # def binary_search(self, start, end):
    #     if end < start:
    #         return start
    #     mid = (start + end) // 2
    #     if self.nums[mid] < self.target:
    #         return self.binary_search(mid + 1, end)
    #     else:
    #         # 即使相等也再向左边区间，为了找左边界
    #         return self.binary_search(start, mid - 1)
    def binary_search(self, start, end):
        if end < start:
            return end
        mid = (start + end) // 2
        if self.nums[mid] > self.target:
            return self.binary_search(start, mid - 1)
        else:
            return self.binary_search(mid + 1, end)

    def searchRange(self, nums, target):
        """
        34.在排序数组中查找元素的第一个和最后一个位置
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        # 初始化
        self.nums = [num for num in nums]
        self.target = target
        # 二分查找：先找左边界再找右边界
        # left = self.binary_search(0, len(self.nums) - 1)
        # if self.nums[left] != self.target:
        #     return [-1, -1]
        # self.target += 1
        # right = self.binary_search(left, len(self.nums) - 1) - 1
        # return [left, right]
        # 二分查找：先找右边界再找左边界
        right = self.binary_search(0, len(self.nums) - 1)
        if self.nums[right] != self.target:
            return [-1, -1]
        self.target -= 1
        left = self.binary_search(0, right) + 1
        return [left, right]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=7))
