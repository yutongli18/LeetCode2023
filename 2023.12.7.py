"""
0-1背包问题。
注意 Python 如何处理输入
"""


class Solution:
    def bag_problem(self, w, v, bag_weight):
        """
        0-1 背包问题
        :param w: List[int]
        :param v: List[int]
        :param bag_weight: int
        :return: int
        """
        dp = [[0 for _ in range(bag_weight + 1)] for _ in range(len(w))]
        for j in range(1, bag_weight + 1):
            # j 是背包重量
            if j >= w[0]:
                dp[0][j] = v[0]
        for i in range(1, len(w)):
            for j in range(1, bag_weight + 1):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i] if j >= w[i] else 0)
        return dp[-1][-1]


if __name__ == '__main__':
    _, bag_weight = [int(num) for num in input().split()]
    weight = [int(num) for num in input().split()]
    value = [int(num) for num in input().split()]
    sol = Solution()
    print(sol.bag_problem(w=weight, v=value, bag_weight=bag_weight))
