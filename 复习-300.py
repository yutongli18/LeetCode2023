class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS(nums=[0]))
