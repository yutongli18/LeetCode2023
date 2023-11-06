"""
46. 全排列
回溯法，注意和组合问题的区别。
"""


class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_result = []
        # used_dict 必须是一个全局的，因为去重在每条路径上，而不是每层
        self.used_dict = {}

    def get_permute(self, nums):
        if len(self.curr_result) == len(nums):
            self.result_list.append(self.curr_result[:])
            return
        for index in range(0, len(nums)):
            if not self.used_dict[nums[index]]:
                self.curr_result.append(nums[index])
                self.used_dict[nums[index]] = True
                self.get_permute(nums[:])
                self.used_dict[nums[index]] = False
                self.curr_result.pop(-1)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.used_dict = {num: False for num in nums}
        self.get_permute(nums)
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute(nums=[1, 2, 3]))
