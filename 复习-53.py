class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = sum(nums)
        count = 0
        for index in range(len(nums)):
            count += nums[index]
            max_sum = max(max_sum, count)
            if count < 0:
                count = 0
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray(nums=[-1]))
