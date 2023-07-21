"""
15.三数之和
双指针
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        i = 0  # 记录查找下标
        move_left, move_right = False, False  # 标志位：是否移动左右指针
        result_list = []  # 存放结果
        while i < length - 2:
            left, right = i + 1, length - 1
            pre_i, pre_left, pre_right = nums[i], nums[left], nums[right]  # 去重
            target = 0 - nums[i]
            while left < right:
                # print(i, left, right)
                # print(move_left, move_right)
                if nums[left] + nums[right] == target:
                    result_list.append([nums[i], nums[left], nums[right]])
                    move_left, move_right = True, True
                elif nums[left] + nums[right] < target:
                    move_left = True
                else:
                    move_right = True
                if move_left:
                    move_left = False
                    while left < right and nums[left] == pre_left:
                        left += 1
                    if left < right:
                        pre_left = nums[left]
                if move_right:
                    move_right = False
                    while left < right and nums[right] == pre_right:
                        right -= 1
                    if left < right:
                        pre_right = nums[right]
            while i < length - 2 and nums[i] == pre_i:
                i += 1
            if i < length - 2:
                pre_i = nums[i]
        return result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
