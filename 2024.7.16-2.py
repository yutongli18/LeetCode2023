class Solution(object):
    def __init__(self):
        self.nums = []
        self.is_visited = {}
        self.curr_result = []
        self.results = []

    def trace_back(self):
        for num in self.nums:
            if not self.is_visited[num]:
                self.curr_result.append(num)
                self.is_visited[num] = True
                if len(self.curr_result) == len(self.nums):
                    self.results.append(self.curr_result[:])
                else:
                    self.trace_back()
                self.is_visited[num] = False
                self.curr_result.pop()

    def permute(self, nums):
        """
        46.全排列
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = [num for num in nums]
        # 整体去重
        for i in range(-10, 11):
            self.is_visited.setdefault(i, False)
        # 回溯法
        self.trace_back()
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([0, 1]))
