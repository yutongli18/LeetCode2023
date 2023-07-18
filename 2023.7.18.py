"""
1. 两数之和
哈希表（字典）
注意：
① dict 中 key 和 value 分别是什么？
把 key 设置成要找的值（或者遍历过的值），value 设置成下标，会比反过来的设计节省时间。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res_dict = {}
        for i in range(len(nums)):
            if res_dict.get(nums[i]) is not None:
                return [res_dict[nums[i]], i]
            res_dict[target - nums[i]] = i


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
