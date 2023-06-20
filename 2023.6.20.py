"""
39.组合总和
回溯法。
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result, path = [], []  # 结果和路径

        def backtrack(candidates, combine, target, idx):
            if combine > target:
                return
            if combine == target:
                return result.append(path[:])
            for i in range(idx, len(candidates)):
                if combine + candidates[i] > target:
                    return
                combine += candidates[i]
                path.append(candidates[i])
                backtrack(candidates, combine, target, i)  # 产生一条路径
                combine -= candidates[i]
                path.pop()

        candidates.sort()
        backtrack(candidates, 0, target, 0)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
