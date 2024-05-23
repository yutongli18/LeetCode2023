class Solution(object):
    def reverse(self, nums, start, end):
        """
        翻转 nums 中从 start 到 end 的部分
        :param nums: list[int]
        :param start: int
        :param end: int
        :return: None
        """
        left, right = start, end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums, k):
        """
        189.轮转数组
        找规律
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol = Solution()
    sol.rotate(nums, 3)
    print(nums)
