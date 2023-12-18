"""
377.组合总和 IV
因为不要求写出所有的组合，所以可以用动态规划来求解。
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for j in range(target + 1):
            for i in range(1, len(nums) + 1):
                if j >= nums[i - 1]:
                    dp[j] += dp[j - nums[i - 1]]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum4(nums=[1, 2, 3], target=4))
