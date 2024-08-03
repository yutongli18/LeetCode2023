class Solution:
    def matrixMultiply(self, dims):
        # 矩阵个数
        n = len(dims) - 1
        # dp[i][j] 从矩阵i到矩阵j的最小连乘操作次数
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        split = [["" for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if j == i:
                    dp[i][j] = 0
                    split[i][j] = str(i)
                else:
                    min_split = -1
                    for k in range(i, j):
                        num_ops = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                        if dp[i][j] == -1:
                            dp[i][j] = num_ops
                            min_split = k
                        else:
                            if num_ops < dp[i][j]:
                                dp[i][j] = num_ops
                                min_split = k
                    split[i][j] = "(" + split[i][min_split] + ")(" + split[min_split + 1][j] + ")"
        return dp[0][-1], split[0][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.matrixMultiply([5, 2, 4, 3, 5]))
