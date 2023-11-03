"""
491. 递增子序列
这个题目有个陷阱，不能像是子集 II 那样去重，因为不能对原始数组进行排序，会破坏题目的要求。
因此只能用一个字典去记录该元素是否搜索过，如果搜索过就跳过。
"""


class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_result = []

    def find_subsequences(self, nums, start_index):
        if len(self.curr_result) >= 2:
            self.result_list.append(self.curr_result[:])
        # 这个 used_dict 不作为参数传递，也不能放在全局的 init 里面
        # 因为它只管层去重，而不是整棵树去重。
        used_dict = {}
        for index in range(start_index, min(len(self.curr_result) + len(nums) - 1, len(nums))):
            used_dict.setdefault(nums[index], False)
            if used_dict[nums[index]]:
                continue
            used_dict[nums[index]] = True
            if self.curr_result and nums[index] < self.curr_result[-1]:
                continue
            self.curr_result.append(nums[index])
            self.find_subsequences(nums, index + 1)
            self.curr_result.pop(-1)

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.find_subsequences(nums, 0)
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubsequences(nums=[1, 1, 1, 1, 1]))
