"""
922.按奇偶排序数组 II
奇数位偶数位遍历
"""


class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even, odd = 0, 1  # 偶数位指针，奇数位指针
        while even < len(nums) and odd < len(nums):
            if nums[even] % 2 != 0:
                while odd < len(nums) and nums[odd] % 2 != 0:
                    odd += 2
                if odd < len(nums):
                    nums[odd], nums[even] = nums[even], nums[odd]
            even += 2
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArrayByParityII(nums=[2, 3]))
