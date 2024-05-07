class Solution(object):
    def reverse_list(self, nums, start, end):
        """
        将 nums 数组中从 start 到 end 这一段反转
        :type nums: list[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        left, right = start, end
        while left < right < len(nums):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def nextPermutation(self, nums):
        """
        31.下一个排列
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        # 从数组最右边开始遍历
        right = len(nums) - 1
        while right >= 1 and nums[right] <= nums[right - 1]:
            right -= 1
        # 如果整个数组都是降序排列的话，不存在下一个排列
        if right < 1:
            nums.reverse()
            return
        # 创建下一个排列
        # 要交换的是 nums[right - 1] 和其右边数组中比它大的最小值
        # 当右边有值相等时，优先换最后出现的一个
        min_max = nums[right]
        min_max_index = right
        temp = right
        while temp < len(nums):
            if nums[right - 1] < nums[temp] <= min_max:
                min_max = nums[temp]
                min_max_index = temp
            temp += 1
        nums[right - 1], nums[min_max_index] = nums[min_max_index], nums[right - 1]
        # 然后把 nums[right - 1] 的右侧升序排列
        self.reverse_list(nums=nums, start=right, end=len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1]
    sol.nextPermutation(nums=nums)
    print(nums)
