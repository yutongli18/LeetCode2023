"""
57.爬楼梯
完全背包。
"""


class Solution:
    def stairs(self, m, n):
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        # 其实这里就是完全背包的滚动数组方法
        # 外层就是遍历背包容量
        # 内层就是遍历物品
        for i in range(2, n + 1):
            for j in range(1, min(i + 1, m + 1)):
                dp[i] += dp[i - j]
        return dp[-1]


if __name__ == '__main__':
    n, m = [int(num) for num in input().split()]
    sol = Solution()
    print(sol.stairs(m=m, n=n))
