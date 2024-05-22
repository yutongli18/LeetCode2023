class Solution(object):
    def maxSubArray(self, nums):
        """
        53.最大子数组和
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray(nums=[-2, 1]))
