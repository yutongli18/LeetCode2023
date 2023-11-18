class Solution(object):
    def __init__(self):
        self.results = []
        self.curr_result = []
        self.used = []

    def get_permute_unique(self, nums):
        if len(self.curr_result) == len(nums):
            self.results.append(self.curr_result[:])
            return
        for index in range(len(nums)):
            if self.used[index]:
                continue
            if index > 0 and nums[index] == nums[index - 1] and not self.used[index - 1]:
                continue
            self.curr_result.append(nums[index])
            self.used[index] = True
            self.get_permute_unique(nums=nums)
            self.curr_result.pop(-1)
            self.used[index] = False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 注意要排序
        nums.sort()
        self.used = [False] * len(nums)
        self.get_permute_unique(nums=nums)
        return self.results


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique(nums=[1]))
