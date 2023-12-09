"""
416. 分割等和子集
0-1背包问题。
nums 既是价值也是重量。
注意判断条件。
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1] if j >= nums[i - 1] else 0)
                if j == target and dp[i][j] == target:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition(nums=[14, 9, 8, 4, 3, 2]))
