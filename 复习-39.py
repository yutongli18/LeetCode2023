class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_result = []

    def get_combination(self, candidates, start_index, rest):
        if rest == 0:
            self.result_list.append(self.curr_result[:])
        for index in range(start_index, len(candidates)):
            if rest - candidates[index] < 0:
                break
            rest -= candidates[index]
            self.curr_result.append(candidates[index])
            self.get_combination(candidates, index, rest)
            rest += candidates[index]
            self.curr_result.pop(-1)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted_candidates = sorted(candidates)
        self.get_combination(sorted_candidates, 0, target)
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
