"""
78. 子集
子集问题和组合或分割问题的不同之处在于，要收集的是所有的情况，也即树上所有的节点，而不仅仅是叶子节点（当终止条件满足时的节点）
"""


class Solution(object):
    def __init__(self):
        self.result_list = [[]]
        self.curr_result = []

    def get_subsets(self, nums, start_index):
        for index in range(start_index, len(nums)):
            self.curr_result.append(nums[index])
            self.result_list.append(self.curr_result[:])
            self.get_subsets(nums[:], index + 1)
            self.curr_result.pop(-1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.get_subsets(nums[:], 0)
        return self.result_list[:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets(nums=[1, 2, 3]))
