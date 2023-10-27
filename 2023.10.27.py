"""
39. 组合总和
有重复的回溯法，注意控制开始索引。
"""


class Solution(object):
    def __init__(self):
        self.curr_combine = []
        self.result_list = []

    def getCombine(self, candidates, rest, start_index):
        if rest == 0:
            self.result_list.append(self.curr_combine[:])
            return
        for index in range(start_index, len(candidates)):
            if rest - candidates[index] < 0:
                # 这里：因为原始数组是无序的，所以不能直接 break 结束循环，只是跳过当前这一枝的遍历。
                continue
            rest -= candidates[index]
            self.curr_combine.append(candidates[index])
            self.getCombine(candidates[:], rest, index)
            rest += candidates[index]
            self.curr_combine.pop(-1)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.getCombine(candidates[:], target, 0)
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum(candidates=[8, 7, 4, 3], target=11))
