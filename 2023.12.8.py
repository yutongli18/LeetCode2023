"""
0-1背包 ①
另一种初始化方式。
"""


class Solution:
    def bag_problem(self, w, v, b):
        """
        求解 0-1 背包问题。
        :param w: List[int] 物品重量
        :param v: List[int] 物品价值
        :param b: int 背包体积
        :return: int
        """
        dp = [[0 for _ in range(b + 1)] for _ in range(len(w) + 1)]
        for i in range(1, len(w) + 1):
            for j in range(1, b + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1] if j >= w[i - 1] else 0)
        return dp[-1][-1]


if __name__ == '__main__':
    _, bag = [int(num) for num in input().split()]
    weight = [int(num) for num in input().split()]
    value = [int(num) for num in input().split()]
    sol = Solution()
    print(sol.bag_problem(w=weight, v=value, b=bag))
