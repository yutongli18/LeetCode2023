"""
0-1 背包
滚动数组。
"""


class Solution:
    def bag_problem(self, w, v, b):
        """
        滚动数组求解 0-1 背包问题。
        :param w: List[int]
        :param v: List[int]
        :param b: int
        :return: int
        """
        dp = [0 for _ in range(b + 1)]
        for i in range(1, len(w) + 1):
            for j in range(b, w[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1] if j >= w[i - 1] else 0)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.bag_problem(w=[2, 2, 3, 1, 5, 2], v=[2, 3, 1, 5, 4, 3], b=1))
