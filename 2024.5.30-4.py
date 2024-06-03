class Solution:
    def minCount(self, height):
        dp = [-1 for _ in range(len(height))]
        dp[0] = 0
        for i in range(1, len(height)):
            for j in range(i):
                if dp[j] == -1:
                    continue
                if height[i] % height[j] == 0:
                    dp[i] = min(dp[i], dp[j] + height[i] // height[j]) if dp[i] != -1 else dp[j] + height[i] // height[j]
                elif height[j] % height[i] == 0:
                    dp[i] = min(dp[i], dp[j] + height[j] // height[i]) if dp[i] != -1 else dp[j] + height[j] // height[i]
        return dp[-1]


if __name__ == '__main__':
    n = int(input())
    height = [int(num) for num in input().split(' ')]
    sol = Solution()
    print(sol.minCount(height=height))
