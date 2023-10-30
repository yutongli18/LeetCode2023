"""
40. 组合总和 II
回溯法。
"""


class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_result = []

    def getCombine(self, candidates, start_index, rest):
        if rest == 0:
            self.result_list.append(self.curr_result[:])
            return

        for index in range(start_index, len(candidates)):
            # 因为排序了，所以后面的元素一定更大，不需要再遍历了
            if rest - candidates[index] < 0:
                break
            # 这里：第一次做的时候比较难想
            # 是对同一层上的数字进行去重，不能用全局的 pre_value 变量来去重，否则全局上的重复元素都不能再选取
            # 同一层上的数字去重，一定发生在 for 循环中
            # index > start_index 是为了在同一层上进行去重
            if index > start_index and candidates[index] == candidates[index - 1]:
                continue
            rest -= candidates[index]
            self.curr_result.append(candidates[index])
            self.getCombine(candidates, index + 1, rest)
            rest += candidates[index]
            self.curr_result.pop(-1)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.getCombine(candidates, start_index=0, rest=target)
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
