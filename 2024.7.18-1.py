class Solution(object):
    def __init__(self):
        self.nums = []
        self.curr = []
        self.curr_sum = 0
        self.results = []

    def trace_back(self, start, target):
        for i in range(start, len(self.nums)):
            if self.curr_sum + self.nums[i] > target:
                return
            self.curr.append(self.nums[i])
            self.curr_sum += self.nums[i]
            if self.curr_sum == target:
                self.results.append(self.curr[:])
            else:
                self.trace_back(i, target)
            self.curr.pop()
            self.curr_sum -= self.nums[i]

    def combinationSum(self, candidates, target):
        """
        39.组合总和
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 初始化
        self.nums = [num for num in candidates]
        self.nums.sort()
        # 回溯
        self.trace_back(0, target)
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2], 1))
