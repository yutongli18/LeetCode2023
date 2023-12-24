"""
0-1 背包
"""


class Solution:
    def bag_problem(self, size, weights, values):
        """dp = [[0 for _ in range(size + 1)] for _ in range(len(weights) + 1)]
        # 递推
        for i in range(1, len(weights) + 1):
            for j in range(1, size + 1):
                if j >= weights[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]"""
        dp = [0 for _ in range(size + 1)]
        for i in range(1, len(weights) + 1):
            for j in range(size, weights[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - weights[i - 1]] + values[i - 1])
        return dp[-1]


if __name__ == '__main__':
    _, bag_size = [int(num) for num in input().split()]
    item_weights = [int(num) for num in input().split()]
    item_values = [int(num) for num in input().split()]
    sol = Solution()
    print(sol.bag_problem(size=bag_size, weights=item_weights, values=item_values))
