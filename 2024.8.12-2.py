class Solution:
    def getMaxWeight(self, distances, weights, capacity):
        n = len(weights) + 1
        weights = [0] + weights
        distances = [0] + distances
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]
        # 背包问题
        for i in range(1, n):
            for j in range(1, capacity + 1):
                cost = weights[i] * distances[i] * 1000
                if j < cost:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + weights[i])
        return dp[n - 1][capacity]


if __name__ == "__main__":
    _, n = [int(num) for num in input().split(" ")]
    weights = [int(num) for num in input().split(" ")]
    distances = [int(num) for num in input().split(" ")]
    sol = Solution()
    print(sol.getMaxWeight(distances, weights, 38000))
