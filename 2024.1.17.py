"""
53.最大子数组和
我感觉这个题目动态规划和贪心没什么太大区别，就是把原本需要递推公式判断的地方变成了用规则判断而已。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            result = max(result, dp[i])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
