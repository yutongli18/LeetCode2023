"""
494. 目标和
动态规划：注意如何初始化 dp 数组。
"""


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        if sum(nums) < abs(target):  # 数组中的元素最大也不能凑到 target
            return count
        if (sum(nums) + target) % 2 > 0:  # 不能构造成功
            return count
        bag_size = (sum(nums) + target) // 2
        dp = [[0 for _ in range(bag_size + 1)] for _ in range(len(nums) + 1)]
        # 这个题目的初始化和普通的 0-1 背包不同
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(bag_size + 1):
                if j >= nums[i - 1]:  # 当选中 nums[i - 1] 时
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTargetSumWays(nums=[0, 0, 0, 0, 0, 0, 0, 0, 1], target=1))
