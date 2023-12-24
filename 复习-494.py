"""
494.目标和
"""


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 还有一个初始判断条件：
        # 如果把 nums 中所有的数字均设置为正或设置为负还不能满足 target 的话，说明不能达成目标和
        if sum(nums) < abs(target):
            return 0
        if (sum(nums) + target) % 2 > 0:
            return 0
        bag_size = (sum(nums) + target) // 2
        # 初始化
        dp = [0 for _ in range(bag_size + 1)]
        dp[0] = 1
        # 递推
        for i in range(len(nums)):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] = dp[j] + dp[j - nums[i]]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
