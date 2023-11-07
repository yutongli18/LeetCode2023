"""
47. 全排列 II
排列问题树层去重的方法。
"""


class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_list = []
        self.used = []

    def get_permute(self, nums):
        if len(self.curr_list) == len(nums):
            self.result_list.append(self.curr_list[:])
            return
        for index in range(0, len(nums)):
            # 在什么情况下，才能在上一个还没被选择的时候，选择了当前的 index 呢，只能说明上一个已经被遍历过了
            if index > 0 and nums[index] == nums[index - 1] and not self.used[index - 1]:
                continue
            if not self.used[index]:
                self.used[index] = True
                self.curr_list.append(nums[index])
                self.get_permute(nums[:])
                self.curr_list.pop(-1)
                self.used[index] = False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        self.used = [False] * len(nums)
        self.get_permute(sorted_nums[:])
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique(nums=[2, 2, 1, 1]))
