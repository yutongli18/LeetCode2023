"""
90. 子集 II
回溯法 + 树层去重。
"""


class Solution(object):
    def __init__(self):
        self.result_list = [[]]
        self.curr_list = []

    def get_subsets(self, nums, start_index):
        for index in range(start_index, len(nums)):
            if index > start_index and nums[index] == nums[index - 1]:
                continue
            self.curr_list.append(nums[index])
            self.result_list.append(self.curr_list[:])
            self.get_subsets(nums, index + 1)
            self.curr_list.pop(-1)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        self.get_subsets(sorted_nums, 0)
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup(nums=[0]))
