"""
1039.多边形三角剖分的最低得分
动态规划。设想一个凸多边形i,i+1,...,j-1,j，通过i,j,k分成三个部分如何求分数。
"""


class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        def dp(i, j):
            if j < i + 2:
                return 0
            elif j == i + 2:
                return values[i] * values[i + 1] * values[j]
            else:
                return min([(values[i] * values[j] * values[k] + dp(i, k) + dp(k, j)) for k in
                            range(i + 1, j)])
        n = len(values)
        return dp(0, n - 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minScoreTriangulation(values=[3, 7, 4, 5]))
