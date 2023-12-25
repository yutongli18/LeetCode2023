"""
卡码网56.携带矿石资源
"""


class Solution(object):
    def bag_problem(self, size, weights, values, nums):
        """flat_weights, flat_values = [], []
        for i in range(len(nums)):
            flat_weights.extend([weights[i]] * nums[i])
            flat_values.extend([values[i]] * nums[i])
        # 初始化
        dp = [[0 for _ in range(size + 1)] for _ in range(sum(nums) + 1)]
        # 递推
        for i in range(1, sum(nums) + 1):
            for j in range(1, size + 1):
                if j >= flat_weights[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - flat_weights[i - 1]] + flat_values[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]"""
        # 初始化
        dp = [0 for _ in range(size + 1)]
        for i in range(len(weights)):
            for j in range(size, weights[i] - 1, -1):
                for k in range(1, nums[i] + 1):
                    if j >= k * weights[i]:
                        dp[j] = max(dp[j], dp[j - k * weights[i]] + k * values[i])
        return dp[-1]


if __name__ == '__main__':
    bag_size, n = [int(num) for num in input().split()]
    item_weights = [int(num) for num in input().split()]
    item_values = [int(num) for num in input().split()]
    item_nums = [int(num) for num in input().split()]

    sol = Solution()
    print(sol.bag_problem(size=bag_size, weights=item_weights, values=item_values, nums=item_nums))
