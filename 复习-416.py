"""
416. 分割等和子集
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum % 2 > 0:
            return False
        target = nums_sum // 2
        # 初始化
        dp = [0 for _ in range(target + 1)]
        dp[0] = 0
        # 递推
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                if j == target and dp[j] == target:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition(nums=[1, 5, 11, 5]))
