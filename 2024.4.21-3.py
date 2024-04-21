class Solution(object):
    def minimumOperations(self, grid):
        """
        100290.使矩阵满足条件的最少操作数
        关键问题在于当频率平局的时候，如何选择最佳的数字，因为它会影响到后面的结果。
        动态规划：dp[col][num] 表示第 col 列选择数字 num 时，需要操作的最少次数。
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # 统计每列各个数字的出现频次
        grid_counter = []
        for col in range(n):
            grid_counter.append([0 for _ in range(10)])
            for row in range(m):
                grid_counter[col][grid[row][col]] += 1
        # 动态规划
        dp = [[0 for _ in range(10)] for _ in range(n)]
        for num in range(10):
            # 对第一列做特殊处理
            dp[0][num] = m - grid_counter[0][num]
        for col in range(1, n):
            for num in range(10):
                # 对于第 col 列，当选择 num 作为列统一的元素时
                # 查找上一列中，在没有选择 num 的情况下，最少的操作次数
                pre_min = m * col
                for pre_num in range(10):
                    if pre_num != num:
                        pre_min = min(pre_min, dp[col - 1][pre_num])
                dp[col][num] = pre_min + (m - grid_counter[col][num])
        return min(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumOperations(grid=[[0, 6, 2], [9, 0, 9], [4, 9, 6]]))
