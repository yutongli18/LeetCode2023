class Solution(object):
    def __init__(self):
        self.results = []
        self.nums = []
        self.curr = []

    def trace_back(self, start):
        for i in range(start, len(self.nums)):
            self.curr.append(self.nums[i])
            self.results.append(self.curr[:])
            self.trace_back(i + 1)
            self.curr.pop()

    def subsets(self, nums):
        """
        78.子集
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = [num for num in nums]
        self.results.append([])
        self.trace_back(0)
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
