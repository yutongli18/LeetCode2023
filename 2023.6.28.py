"""
40.组合总和II
回溯法。
步骤：判断是否已经满足条件，满足则直接返回 → 遍历待选数组 → 判断是否超出条件（剪枝） → 产生一条分支 → 递归地在这条分支上寻找答案 →
回溯（包括分支上已经得到的和，已经添加的路径等）
"""


class Solution(object):
    def __init__(self):
        self.paths = []
        self.path = []

    def backTracking(self, candidates, target, sum, startIndex):
        if sum == target:
            self.paths.append(self.path[:])
            return
        for i in range(startIndex, len(candidates)):
            if sum + candidates[i] > target:
                return
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backTracking(candidates, target, sum, i + 1)
            self.path.pop()
            sum -= candidates[i]

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.backTracking(candidates, target, 0, 0)
        return self.paths


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
