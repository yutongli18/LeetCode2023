"""
1186.删除一次得到子数组最大和
动态规划
"""


class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arrLength = len(arr)
        dp_0, dp_1 = arr[0], 0  # 记录dp[i-1][0]和dp[i-1][1]
        result = arr[0]  # 记录答案
        for i in range(1, arrLength):
            new_dp_0 = max(dp_0, 0) + arr[i]  # dp[i][0] = max(dp[i-1][0], 0) + arr[i]
            new_dp_1 = max(dp_1 + arr[i], dp_0)  # dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0])
            dp_0 = new_dp_0
            dp_1 = max(new_dp_0, new_dp_1)
            result = max(result, dp_1)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSum(arr=[2, 1, -2, -5, -2]))
