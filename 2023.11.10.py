"""
53. 最大子数组和
分治法 + 贪心算法（超时）。
贪心算法。
"""


class Solution(object):
    """def get_max(self, nums, start_index, end_index):
        if start_index == end_index:
            return nums[start_index]
        mid_index = int((start_index + end_index) / 2)
        left_max = self.get_max(nums[:], start_index, mid_index)
        right_max = self.get_max(nums[:], mid_index + 1, end_index)
        mid_left_max, mid_right_max = nums[mid_index], nums[mid_index + 1]
        mid_left_sum, mid_right_sum = 0, 0
        for index in range(mid_index, start_index - 1, -1):
            mid_left_sum += nums[index]
            mid_left_max = max(mid_left_max, mid_left_sum)
        for index in range(mid_index + 1, end_index + 1):
            mid_right_sum += nums[index]
            mid_right_max = max(mid_right_max, mid_right_sum)
        mid_max = mid_left_max + mid_right_max
        return max(left_max, right_max, mid_max)"""

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """return self.get_max(nums=nums[:], start_index=0, end_index=len(nums) - 1)"""
        max_sum = nums[0]
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            # 这里：即时更新最大子数组和
            max_sum = max(max_sum, count)
            # 贪心在这里：当和为负数时，表明当前这个元素不能要，那么新的子数组应该从下一个元素再开始
            if count < 0:
                count = 0
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
